# Idle Mafia Precision Mouse Macro — Update Feed

This repository is the public update feed used by the app's **Update Center**.

## Current stable release
**v14.1.0 — App Icon Micro Update**

- `manifest.json` tells installed clients which versions are available.
- `releases/<version>/` contains lightweight version files for newer updates.
- `packages/<version>/` contains packaged update data for older/full releases.
- `CHANGELOG.md` contains the human-readable release history.

The updater verifies SHA-256 hashes before installing downloaded files. App versions are installed side-by-side so an older published version can be selected again from the Update Center, while settings, recordings, and analytics remain in shared app data.
