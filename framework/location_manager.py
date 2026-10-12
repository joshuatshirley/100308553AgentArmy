"""Location knowledge overlay manager for AgentArmy.

Allows recruiting stations, battalions, brigades, MEPS, and state National Guard
units to inject local SOPs, education benefits, and processing guidelines alongside
national Army doctrine.
"""
from __future__ import annotations

import os
import re
from typing import Any, Dict, List, Optional

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LocationManager:
    """Manages location-specific knowledge overlays for recruiting stations and MEPS."""

    def __init__(self, repo_root: Optional[str] = None):
        self.repo_root = repo_root or REPO_ROOT
        self.locations_dir = os.path.join(self.repo_root, "locations")
        self.overlays: List[Dict[str, Any]] = []
        self._load_overlays()

    def _load_overlays(self) -> None:
        if not os.path.exists(self.locations_dir):
            return

        for root, _, files in os.walk(self.locations_dir):
            for file in files:
                if file.endswith(".md") and not file.startswith("_"):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.repo_root).replace("\\", "/")
                    self._parse_overlay_file(full_path, rel_path)

    def _parse_overlay_file(self, full_path: str, rel_path: str) -> None:
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()
        except Exception:
            return

        # Simple front matter parser
        front_matter = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm_text = parts[1]
                body = parts[2].strip()
                for line in fm_text.splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        front_matter[k.strip()] = v.strip().strip('"').strip("'")

        # Determine location type from path or front matter
        loc_type = front_matter.get("type", "")
        if not loc_type:
            if "meps" in rel_path.lower():
                loc_type = "meps"
            elif "states" in rel_path.lower() or "guard" in rel_path.lower():
                loc_type = "state_guard"
            elif "stations" in rel_path.lower():
                loc_type = "station"
            elif "battalions" in rel_path.lower():
                loc_type = "battalion"
            else:
                loc_type = "general"

        title = front_matter.get("title", os.path.splitext(os.path.basename(rel_path))[0].replace("_", " ").title())
        location_id = front_matter.get("id", os.path.splitext(os.path.basename(rel_path))[0])
        applicable_agents = [
            a.strip()
            for a in front_matter.get("applicable_agents", "").split(",")
            if a.strip()
        ]
        aliases = [
            alias.strip().lower()
            for alias in front_matter.get("aliases", "").split(",")
            if alias.strip()
        ]
        # Include default aliases from title and id
        aliases.append(location_id.lower().replace("_", " "))
        aliases.append(title.lower())

        self.overlays.append({
            "id": location_id,
            "title": title,
            "type": loc_type,
            "applicable_agents": applicable_agents,
            "aliases": list(set(aliases)),
            "rel_path": rel_path,
            "body": body,
        })

    def detect_locations(self, text: str) -> List[Dict[str, Any]]:
        """Detect any location mentions inside a user query or station context."""
        text_lower = text.lower()
        matches = []
        for overlay in self.overlays:
            for alias in overlay["aliases"]:
                if alias and alias in text_lower:
                    matches.append(overlay)
                    break
        return matches

    def get_overlays_for_agent(
        self, agent_id: str, location_hint: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Find overlays relevant to a specific agent, filtered optionally by location query/hint."""
        active = []
        detected = self.detect_locations(location_hint) if location_hint else self.overlays

        for ov in detected:
            # If overlay explicitly specifies applicable agents, check match
            if ov["applicable_agents"]:
                if agent_id in ov["applicable_agents"] or "all" in ov["applicable_agents"]:
                    active.append(ov)
            else:
                # By default, match if location was detected in query
                active.append(ov)

        return active
