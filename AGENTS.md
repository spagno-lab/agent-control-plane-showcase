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
- This public repository treats fork/PR code as untrusted. GitHub Actions uses
  ephemeral GitHub-hosted Linux runners with digest-pinned job containers and
  SHA-pinned actions. PR validation has read-only contents permission, receives
  no production authority and cannot deploy. Pages write/OIDC permission exists
  only in the trusted push/manual deploy job. A persistent self-hosted runner is
  not required and must not be introduced merely for cross-repository uniformity.
