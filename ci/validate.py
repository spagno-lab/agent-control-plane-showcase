#!/usr/bin/env python3
"""Validate the static publication and public-repository trust boundary."""

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
    assert "pull_request_target" not in workflow
    assert workflow.count("runs-on:") == 2
    assert workflow.count("runs-on: ubuntu-24.04") == 2
    assert workflow.count("container:") == 2
    assert "self-hosted" not in workflow
    assert "permissions:\n  contents: read" in workflow

    policy, deploy = workflow.split("  deploy:", maxsplit=1)
    assert "pages: write" not in policy
    assert "id-token: write" not in policy
    assert "environment:" not in policy
    assert deploy.count("pages: write") == 1
    assert deploy.count("id-token: write") == 1
    assert "github.event_name == 'push'" in deploy
    assert "github.event_name == 'workflow_dispatch'" in deploy
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
        "secrets.",
        "kubectl ",
        "vault ",
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
