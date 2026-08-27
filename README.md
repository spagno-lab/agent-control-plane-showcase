# Agent Control Plane showcase

A public, sanitized architecture case study for a declarative control plane that turns human goals into bounded agent work and independently verifies the resulting external state.

The site is intentionally lightweight: semantic HTML, responsive CSS, and a small progressive-enhancement script. GitHub Pages deploys the static files through GitHub Actions.

## Run locally

No build step is required. Serve the repository root with any static file server, for example:

```sh
python3 -m http.server 8080
```

Then open `http://localhost:8080`.

## Deployment

Pushes to `main` trigger `.github/workflows/pages.yml`. The workflow configures Pages, uploads the repository as a Pages artifact, and deploys it to the `github-pages` environment.

## Publication boundary

This repository contains selected public concepts only. It does not mirror internal implementation, operational state, credentials, private identifiers, infrastructure names, or execution records.

## License

MIT
