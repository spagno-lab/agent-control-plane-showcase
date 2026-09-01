#!/usr/bin/env python3
"""Validate the static publication boundary and container-only CI contract."""

from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/pages.yml"
ACTION = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")
DIGEST = re.compile(r"^[^\s]+@sha256:[0-9a-f]{64}$")


def main() -> None:
    workflow = WORKFLOW.read_text(encoding="utf-8")
    assert not re.search(r"runs-on:\s*(?:ubuntu|windows|macos)-", workflow)
    assert workflow.count("runs-on:") == 2
    assert workflow.count("container:") == 2
    assert workflow.count("- self-hosted") == 2
    assert workflow.count("- linux") == 2
    for image in re.findall(r"^\s+image:\s+(\S+)$", workflow, re.MULTILINE):
        assert DIGEST.fullmatch(image), image
        assert ":latest@" not in image
    for action in re.findall(r"^\s+uses:\s+(\S+)", workflow, re.MULTILINE):
        if action.startswith("docker://"):
            assert DIGEST.fullmatch(action.removeprefix("docker://")), action
        else:
            assert ACTION.fullmatch(action), action
    forbidden = (
        "sudo ",
        "apt-get install",
        "pip install",
        "npm install -g",
        "/var/run/docker.sock",
        "secrets: inherit",
    )
    assert not any(item in workflow for item in forbidden)

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    HTMLParser().feed(html)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for required in ("PostgreSQL", "Memory Service", "IMPLEMENTED", "TARGET", "BLOCKED"):
        assert required in readme, required
    for stale in (
        "interim manual Job relay",
        "Next</span><h3>Event-driven dispatcher",
        "Goal controller</b><span>Observe · Compare · Reconcile",
    ):
        assert stale not in html, stale
    for asset in ("styles.css", "script.js", ".nojekyll"):
        assert (ROOT / asset).is_file(), asset


if __name__ == "__main__":
    main()
