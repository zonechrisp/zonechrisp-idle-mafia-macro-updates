# Changelog

## v14.0.0 — Update Center
Released: 2026-09-07

- Added an in-app Update Center with automatic update checks.
- Added startup update popups with **Update Now**, **View Changes**, and **Later**.
- Added a full version-history view and the ability to install or switch back to older published versions.
- App versions are stored side-by-side under `versions/`, while settings, recordings, and analytics remain in the shared `data/` folder.
- Added SHA-256 verification for every downloaded update package before it can be installed.
- Added Stable/Beta channel selection for future releases.
- Added a stable launcher so future versions can be selected without re-extracting the entire app.

## v13

- Added configurable SECRET / MYTHIC / BOTH stop conditions.
- Added subtle UI animations and general performance optimizations.
- Improved precision mouse playback and rare-detection responsiveness.
