#!/usr/bin/env python3
from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
archive_text = ROOT / "artifacts" / "mapes-agent-persona-eval.zip.b64"
output_zip = ROOT / "artifacts" / "mapes-agent-persona-eval.zip"

data = "".join(archive_text.read_text(encoding="utf-8").split())
output_zip.write_bytes(base64.b64decode(data))
print(f"Restored: {output_zip}")
print("Unzip this archive to recover the complete generated project folder.")
