# AGENTS.md — Agent Control Plane showcase

This repository is a public, sanitized explanation of Agent Platform concepts.
It is not runtime authority, deployment state, or an operational audit store.

- Keep desired architecture visibly distinct from implemented and live-verified
  behavior.
- Do not publish credentials, private identifiers, infrastructure names, raw
  execution records, or personal deployment details.
- ACP owns Goal/Job/Worker/Run execution authority. Memory Service is a separate
  durable-context authority with separate per-client credentials.
- Do not describe Goal-level convergence, clean-room enrollment, a Kubernetes
  operator, or low-latency runtime feedback as live unless independently
  verified evidence exists.
- **TARGET:** GitHub Actions workload jobs use self-hosted Linux runners and
  digest-pinned job containers. The current Pages workflow remains
  GitHub-hosted until this public repository has an eligible self-hosted runner.
