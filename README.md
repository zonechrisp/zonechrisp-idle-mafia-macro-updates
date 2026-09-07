# Roblox Auto Roll Selector — Update Feed

This repository is the public update feed used by the app's **Update Center**. The repository name is legacy from the original Idle Mafia-only versions; the current app is designed for Roblox roll/selection workflows more generally.

## Release channels

**Stable: v16.2.0 — In-App Recording Countdown**

v16.2.0 is intentionally the only Stable release.

**Beta: v17.1.1 — Purple UI & Scroll Stability**

The Beta line contains the universal Roblox features: custom Smart Vision templates, mouse + keyboard macro recording, 10 sequence slots, Popup Recovery, and the newer interface. v17.1.1 also fixes scroll rendering artifacts, adds the purple branding, removes Analytics, and expands Help & Guide.

Users on v17.x should select **Beta** in the Update Center to receive newer v17 releases. Stable shows only v16.2.0.

- `manifest.json` tells installed clients which versions and channels are available.
- `packages/<version>/` contains Base64-chunked update packages used by the in-app updater.
- `CHANGELOG.md` contains the human-readable release history.

The updater concatenates the declared package chunks, decodes the ZIP, and verifies its SHA-256 hash before installation. App versions are installed side-by-side while settings, macros, uploaded target images, Popup Recovery data, and sequence data remain in shared app data.
