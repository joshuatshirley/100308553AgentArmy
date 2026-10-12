"""High-performance doctrine retriever for AgentArmy.

Loads catalog/source_catalog.json, catalog/usarec_message_catalog.json, and
extracts exact chapter and paragraph texts from doctrine/*.md.
"""
from __future__ import annotations

import json
import os
import re
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DoctrineRetriever:
    """Retriever for Army recruiting doctrine chapters, paragraphs, and USAREC messages."""

    def __init__(self, repo_root: Optional[str] = None):
        self.repo_root = repo_root or REPO_ROOT
        self.catalog_path = os.path.join(self.repo_root, "catalog", "source_catalog.json")
        self.messages_path = os.path.join(self.repo_root, "catalog", "usarec_message_catalog.json")

        self.catalog: Dict[str, Any] = {}
        self.messages: Dict[str, Any] = {}
        self._file_cache: Dict[str, str] = {}

        self._load_catalogs()

    def _load_catalogs(self) -> None:
        if os.path.exists(self.catalog_path):
            with open(self.catalog_path, "r", encoding="utf-8") as f:
                self.catalog = json.load(f)
        if os.path.exists(self.messages_path):
            with open(self.messages_path, "r", encoding="utf-8") as f:
                self.messages = json.load(f)

    def read_file(self, rel_path: str) -> str:
        """Read a markdown or text file relative to repo root with caching."""
        clean_rel = rel_path.replace("\\", "/").lstrip("/")
        if clean_rel in self._file_cache:
            return self._file_cache[clean_rel]

        full_path = os.path.join(self.repo_root, clean_rel)
        if not os.path.exists(full_path):
            return ""

        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
            self._file_cache[clean_rel] = content
            return content
        except Exception:
            return ""

    def get_doc(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Return catalog entry for a document."""
        return self.catalog.get(doc_id)

    def find_paragraph_location(self, doc_id: str, paragraph_num: str) -> Optional[Tuple[str, str, str]]:
        """Find the (chapter_id, file_path, paragraph_title) for a given doc and paragraph number."""
        doc = self.get_doc(doc_id)
        if not doc:
            return None

        chapters = doc.get("chapters", {})
        norm_para = paragraph_num.strip().replace("–", "-")

        for ch_id, ch_info in chapters.items():
            paras = ch_info.get("paragraphs", {})
            for p_num, p_info in paras.items():
                if p_num.replace("–", "-") == norm_para:
                    title = p_info.get("title", "") if isinstance(p_info, dict) else str(p_info)
                    return ch_id, ch_info.get("file", ""), title

        return None

    def extract_paragraph_text(self, doc_id: str, paragraph_num: str) -> Optional[Dict[str, Any]]:
        """Extract the exact body text of a paragraph from its chapter markdown file."""
        loc = self.find_paragraph_location(doc_id, paragraph_num)
        if not loc:
            return None

        ch_id, file_path, title = loc
        content = self.read_file(file_path)
        if not content:
            return None

        norm_para = paragraph_num.strip().replace("–", "-")
        escaped_num = re.escape(norm_para).replace(r"\-", r"[\-–—]")
        pattern = re.compile(rf"(?:^|\n)(?:[#]+\s*)?({escaped_num}\.?\s+[^\n]+)", re.MULTILINE)

        match = pattern.search(content)
        if not match:
            pattern_fallback = re.compile(rf"(?:^|\n)(?:[#]+\s*)?({escaped_num}\.?[^\n]*)", re.MULTILINE)
            match = pattern_fallback.search(content)
            if not match:
                return {
                    "doc_id": doc_id,
                    "paragraph": paragraph_num,
                    "title": title,
                    "file": file_path,
                    "text": f"Paragraph {paragraph_num} heading found in catalog ({title}), but body could not be isolated from {file_path}.",
                }

        start_pos = match.start()
        next_para_pattern = re.compile(
            r"(?:\n[#]{1,3}\s+[^\n]+|\n\d+[\-–—]\d+\.\s+[A-Z]|\n[A-Z][a-z]+ [I|V|X]+|\nChapter \d+)",
            re.MULTILINE,
        )

        search_after = match.end()
        next_match = next_para_pattern.search(content, search_after)
        if next_match:
            end_pos = next_match.start()
            para_text = content[start_pos:end_pos].strip()
        else:
            para_text = content[start_pos : start_pos + 5000].strip()

        return {
            "doc_id": doc_id,
            "chapter": ch_id,
            "paragraph": paragraph_num,
            "title": title,
            "file": file_path,
            "text": para_text,
        }

    def get_agent_sources_text(
        self, agent_seed: Dict[str, Any], max_chars_per_para: int = 4000
    ) -> List[Dict[str, Any]]:
        """Gather all cited paragraph and document texts for a specialist agent seed."""
        results = []
        sources = agent_seed.get("sources", [])

        for s in sources:
            doc_id = s.get("doc")
            if not doc_id:
                continue

            doc_title = s.get("title", doc_id)
            paragraphs = s.get("paragraphs", {})
            markdown_file = s.get("markdown", "")

            if paragraphs and isinstance(paragraphs, dict):
                for p_num, p_name in paragraphs.items():
                    extracted = self.extract_paragraph_text(doc_id, p_num)
                    if extracted and extracted.get("text"):
                        text = extracted["text"]
                        if len(text) > max_chars_per_para:
                            text = text[:max_chars_per_para] + "\n...[truncated]"
                        results.append({
                            "doc_id": doc_id,
                            "doc_title": doc_title,
                            "paragraph": p_num,
                            "paragraph_title": p_name,
                            "file": extracted.get("file", markdown_file),
                            "text": text,
                        })
                    else:
                        results.append({
                            "doc_id": doc_id,
                            "doc_title": doc_title,
                            "paragraph": p_num,
                            "paragraph_title": p_name,
                            "file": markdown_file,
                            "text": f"[{doc_id} {p_num} {p_name}]",
                        })
            elif markdown_file:
                file_text = self.read_file(markdown_file)
                if file_text:
                    snippet = file_text[:max_chars_per_para].strip()
                    results.append({
                        "doc_id": doc_id,
                        "doc_title": doc_title,
                        "chapter": s.get("chapter", "all"),
                        "chapter_title": s.get("chapter_title", ""),
                        "file": markdown_file,
                        "text": snippet + ("\n...[truncated]" if len(file_text) > max_chars_per_para else ""),
                    })

        return results

    def get_usarec_messages_info(self, message_refs: List[Any]) -> List[Dict[str, Any]]:
        """Get structured info and currency flags for USAREC messages."""
        msg_list = []
        for ref in message_refs:
            num = ref.get("number") if isinstance(ref, dict) else str(ref)
            num_clean = num.replace("USAREC_MESSAGE_", "").replace("USAREC Message ", "").strip()

            msg_data = self.messages.get(num_clean) or self.messages.get(f"USAREC_MESSAGE_{num_clean}")
            if msg_data:
                msg_list.append({
                    "number": num_clean,
                    "subject": msg_data.get("subject", ref.get("subject", "") if isinstance(ref, dict) else ""),
                    "status": msg_data.get("status", "active"),
                    "rescinded_by": msg_data.get("rescinded_by"),
                    "review_flag": msg_data.get("review_flag", False),
                    "note": ref.get("note", "") if isinstance(ref, dict) else "",
                })
            else:
                msg_list.append({
                    "number": num_clean,
                    "subject": ref.get("subject", "") if isinstance(ref, dict) else "",
                    "status": "unverified",
                    "review_flag": False,
                })
        return msg_list

    def search_doctrine(self, query: str, doc_ids: Optional[List[str]] = None, max_results: int = 5) -> List[Dict[str, Any]]:
        """Keyword search across cataloged paragraphs to find citable doctrine."""
        tokens = [t.lower() for t in re.findall(r"\w+", query) if len(t) > 2]
        if not tokens:
            return []

        hits = []
        target_docs = doc_ids or list(self.catalog.keys())

        for d_id in target_docs:
            doc = self.catalog.get(d_id)
            if not doc:
                continue

            chapters = doc.get("chapters", {})
            for ch_id, ch_info in chapters.items():
                paras = ch_info.get("paragraphs", {})
                for p_num, p_info in paras.items():
                    title = p_info.get("title", "") if isinstance(p_info, dict) else str(p_info)
                    score = 0
                    title_lower = title.lower()
                    for token in tokens:
                        if token in title_lower:
                            score += 5
                        if token == p_num.lower():
                            score += 15

                    if score > 0:
                        hits.append({
                            "doc_id": d_id,
                            "doc_title": doc.get("title", d_id),
                            "chapter": ch_id,
                            "paragraph": p_num,
                            "paragraph_title": title,
                            "file": ch_info.get("file", ""),
                            "score": score,
                        })

        hits.sort(key=lambda x: x["score"], reverse=True)
        return hits[:max_results]
