# Agent Control Plane showcase

A public, sanitized architecture case study for a vendor-neutral control plane
that turns human goals into bounded agent work. It distinguishes current
runtime authority from the still-targeted Goal reconciliation loop.

## Current status boundary

- **IMPLEMENTED:** PostgreSQL-authoritative Goal, Job, Worker, Run and Event
  state; atomic claims; leases; fencing; heartbeats; checkpoints; retries; a
  polling dispatcher; Worker/Orchestrator authorization; and public MCP
  surfaces.
- **IMPLEMENTED:** Memory Service is an independent durable-context authority.
  ACP and Memory issue separate per-client credentials; Memory is not a queue or
  runtime authority.
- **VERIFIED:** source, PostgreSQL integration, protocol, container, and
  reference-deployment route/readiness evidence for the released components.
- **TARGET:** a level-based Goal controller that independently observes external
  success criteria and owns Goal Ready convergence; low-latency runtime event
  streaming; and an optional Kubernetes operator projection.
- **BLOCKED:** live clean-room Worker/Orchestrator enrollment in the reference
  deployment until the first authorized root Orchestrator ceremony is performed.

## What the case study covers

- Goal-oriented orchestration with durable Job and Run history.
- Fail-closed reference resolution: a nonexistent Job produces a visible block and zero external mutation.
- Operational Jobs that carry capabilities, audit mode, reversible-change authority, protected control paths, approvals, verification and rollback as explicit fields.
- A target reconciliation contract in which a successful Job may apply zero
  changes when authoritative evidence proves the desired state already holds.
- Append-only correction of a wrong conclusion, including a failed access attempt attributed to the wrong account.
- Current polling dispatch with database-backed assignment/claim authority.
- Roadmap order: independent Goal reconciliation, low-latency runtime feedback,
  then an optional Kubernetes Operator projection.

The site is intentionally lightweight: semantic HTML, responsive CSS, and a small progressive-enhancement script. GitHub Pages deploys the static files through GitHub Actions.

## Run locally

No build step is required. Serve the repository root with any static file server, for example:

```sh
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Deployment

Pushes to `main` configure Pages, upload the repository as an artifact, and
deploy to the protected `github-pages` environment. Because this repository is
public and pull requests may contain untrusted fork code, validation runs on an
ephemeral GitHub-hosted Linux runner inside a digest-pinned job container with
read-only contents permission and no secret or private-infrastructure access.
Pages write/OIDC authority exists only in the trusted push/manual deploy job.
External actions are commit-pinned; neither job installs host software or
depends on mutable runner-host tooling.

## Publication boundary

This repository contains selected public concepts only. It does not mirror internal implementation, operational state, credentials, private identifiers, infrastructure names, or execution records.

## License

MIT
