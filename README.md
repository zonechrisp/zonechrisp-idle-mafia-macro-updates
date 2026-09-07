# Roblox Auto Roll Selector — Update Feed

This repository is the public update feed used by the app's **Update Center**. The repository name is legacy from the app's original Idle Mafia-only versions; the current app is now universal for Roblox games.

## Current stable release
**v17.0.0 — Universal Roblox Target Engine**

v17 adds user-uploaded visual target templates, optional keyboard recording, and up to 10 independent sequence slots while retaining the low-impact playback engine and existing rollback system.

- `manifest.json` tells installed clients which versions are available.
- `packages/<version>/` contains packaged update data.
- `CHANGELOG.md` contains the human-readable release history.

The updater verifies SHA-256 hashes before installing downloaded files. App versions are installed side-by-side so an older published version can be selected again from the Update Center, while settings, macros, uploaded target images, and sequence data remain in shared app data.
