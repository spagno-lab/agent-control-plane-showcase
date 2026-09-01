# Agent Control Plane showcase

A public, sanitized architecture case study for a vendor-neutral control plane
that turns human goals into bounded agent work. It distinguishes current
runtime authority and the implemented deterministic Goal reconciliation layer
from still-targeted runtime feedback and deployment projections.

## Current status boundary

- **IMPLEMENTED:** PostgreSQL-authoritative Goal, Job, Worker, Run and Event
  state; atomic claims; leases; fencing; heartbeats; checkpoints; retries; a
  polling dispatcher; Worker/Orchestrator authorization; public MCP surfaces;
  and a separate deterministic GoalController v1. The controller creates
  bounded planner/action Jobs, validates schema-versioned results, fences Goal
  generations, deduplicates work and sets Ready only after an explicit
  convergence result.
- **IMPLEMENTED:** Memory Service is an independent durable-context authority.
  ACP and Memory issue separate per-client credentials; Memory is not a queue or
  runtime authority.
- **VERIFIED:** source, PostgreSQL integration, protocol, container, and
  reference-deployment route/readiness evidence for the released components,
  including GoalController health and metrics. PostgreSQL and synthetic
  end-to-end tests prove the controller state machine; an independently
  observed real-agent Goal execution is not claimed here.
- **TARGET:** low-latency runtime event streaming and an optional Kubernetes
  operator projection. Persistent steer/pause/resume/cancel, automatic
  repository mutation leases, and macro-task resume remain product targets.
- **BLOCKED:** independent real-agent GoalController E2E in the reference
  deployment until a safe non-production or explicitly authorized Goal exists;
  this is a verification gate, not a missing controller implementation.

## What the case study covers

- Goal-oriented orchestration with durable Job and Run history.
- Fail-closed reference resolution: a nonexistent Job produces a visible block and zero external mutation.
- Operational Jobs that carry capabilities, audit mode, reversible-change authority, protected control paths, approvals, verification and rollback as explicit fields.
- The implemented reconciliation contract in which a successful planner may
  propose zero changes when authoritative evidence proves the desired state
  already holds.
- Append-only correction of a wrong conclusion, including a failed access attempt attributed to the wrong account.
- Current polling dispatch with database-backed assignment/claim authority.
- Roadmap order: low-latency runtime feedback, then an optional Kubernetes
  Operator projection; repository mutation fencing and macro-task resume remain
  separate targets.

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
