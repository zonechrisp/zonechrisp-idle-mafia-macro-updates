# Changelog

## v14.1.1 — Windows Taskbar Icon Fix
Released: 2026-09-07

- Fixed the app icon not appearing correctly on the Windows taskbar.
- Set the app's Windows AppUserModelID before Tk creates the application window.
- Added native `WM_SETICON` handling for both the small and large Windows icons, including the actual root HWND used by the taskbar.
- Added a multi-size `.ico` fallback generated from the app icon and re-applies it after the window is mapped so Tk/Windows cannot silently replace it.
- Macro playback, rare detection, recordings, and settings are unchanged.

## v14.1.0 — App Icon Micro Update
Released: 2026-09-07

- Added a custom app icon designed for **Idle Mafia Precision Mouse Macro**.
- The icon now appears in the Windows app window and replaces the old **IM** sidebar badge.
- Updated the app title to show the full version number **14.1.0**.
- This is a lightweight visual micro-update; macro playback and rare-detection behavior are unchanged.

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
