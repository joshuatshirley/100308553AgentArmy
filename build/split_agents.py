"""Split ALL_AGENTS.md into one markdown file per agent.

usage: python split_agents.py ALL_AGENTS.md OUT_DIR
Each block between <!-- BEGIN AGENT: id --> and <!-- END AGENT: id --> becomes OUT_DIR/<id>.md.
"""
import os, re, sys

src, out = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
blocks = re.findall(r"<!-- BEGIN AGENT: (\S+) -->\n(.*?)\n<!-- END AGENT: \1 -->", text, flags=re.S)
if not blocks:
    sys.exit("no agent blocks found")
os.makedirs(out, exist_ok=True)
for agent_id, body in blocks:
    with open(os.path.join(out, f"{agent_id}.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(body.rstrip() + "\n")
print(f"wrote {len(blocks)} files to {out}")
