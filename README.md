# Roblox Auto Roll Selector — Update Feed

This repository is the public update feed used by the app's **Update Center**. The repository name is legacy from the app's original Idle Mafia-only versions; the current app is universal for Roblox games.

## Current stable release
**v17.1.0 — Smart Vision & Popup Recovery**

v17.1 adds per-slot popup recovery, a stronger custom-target vision stack that combines structure, colour and text/edge appearance, scale-tolerant matching, and a refreshed Automation Studio interface. It retains the 10-slot sequence engine, mouse + keyboard macro recording, and the low-impact Roblox playback engine.

- `manifest.json` tells installed clients which versions are available.
- `packages/<version>/` contains the Base64-chunked update package used by the in-app updater.
- `CHANGELOG.md` contains the human-readable release history.

The updater concatenates the declared package chunks, decodes the ZIP, and verifies its SHA-256 hash before installation. App versions are installed side-by-side while settings, macros, uploaded target images, popup handlers, and sequence data remain in shared app data.
