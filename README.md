# Idle Mafia Precision Mouse Macro — Update Feed

This repository is the public update feed used by the app's **Update Center**.

- `manifest.json` tells installed clients which versions are available.
- `packages/<version>/` contains the versioned update package data.
- `CHANGELOG.md` contains the human-readable release history.

The updater downloads the package listed in the manifest, reconstructs it locally, and verifies its SHA-256 checksum before it can be installed. App versions are installed side-by-side so an older published version can be selected again from the Update Center.
