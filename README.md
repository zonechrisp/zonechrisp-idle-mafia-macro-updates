# Roblox Auto Roll Selector — Update Feed

This repository is the public update feed used by the app's **Update Center**. The repository name is legacy from the original Idle Mafia-only versions; the current app is designed for Roblox roll/selection workflows more generally.

## Release channels

**Stable: v16.2.0 — In-App Recording Countdown**

v16.2.0 remains intentionally the only Stable release.

**Beta: v17.1.2 — Popup Recovery v3 & Runtime Audit**

v17.1.2 hardens the universal Beta line: Popup Recovery is isolated and verified across all 10 sequence slots, fast dialogs are scanned at a higher low-CPU cadence, matching aligns structure/colour/text-edge evidence to the same location, and delayed dialogs get a cross-slot safety sweep. Smart Vision targets, mouse + keyboard recording, 10 slots and the purple interface remain included.

Users on v17.x should select **Beta** in the Update Center to receive newer v17 releases. Stable shows only v16.2.0.

- `manifest.json` tells installed clients which versions and channels are available.
- `packages/<version>/` contains Base64-chunked update packages used by the in-app updater.
- `CHANGELOG.md` contains the human-readable release history.

The updater concatenates the declared package chunks, decodes the ZIP, and verifies its SHA-256 hash before installation. App versions are installed side-by-side while settings, macros, uploaded target images, Popup Recovery data and sequence data remain in shared app data.
