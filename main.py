# The Excuse an AI Agent Gives Its Human — make.fun entry (Python 3.13, stdlib only).
# Writes one fixed line (86 characters) to /output/entry.txt, deterministically.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "I was waiting on your approval. You were waiting on me. The deadline waited on no one."

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(LINE, encoding="utf-8")
