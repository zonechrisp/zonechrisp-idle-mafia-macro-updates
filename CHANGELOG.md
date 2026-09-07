# Changelog

## v16.2.0 — In-App Recording Countdown
Released: 2026-09-07

- Removed the floating recording-countdown overlay approach that caused issues.
- The main app now **stays visible** while a macro recording countdown is running.
- The existing **Engine status** corner now shows the countdown directly: **REC 2.0s → REC 1.9s → ... → REC 0.1s**.
- Engine status changes to **RECORDING** only after the real mouse listener and recording-stop hotkey are active.
- Updated the recording confirmation so it clearly says the app stays open during the countdown.
- Works for both the legacy single-macro recorder and all five **Sequence Mode** macro slots.
- The configurable **Record countdown (s)** setting is still respected; the default remains 2 seconds.
- Sequence logic, the v15 Low-Impact Game Engine, exact absolute mouse coordinates, rarity detection and saved recordings are unchanged.

## v16.0.0 — Five-Slot Sequence Engine
Released: 2026-09-07

- Added **Sequence Mode** with up to five independent macro + rarity-area pairs.
- Each slot now has its own exact recorded mouse macro, rarity region, enabled state, and **BOTH / SECRET / MYTHIC** stop target.
- The engine rotates through active slots in order: Slot 1 → Slot 2 → Slot 3 → Slot 4 → Slot 5.
- If a slot detects its selected rare, only that slot is immediately stopped and deactivated; all other slots continue.
- Auto-deactivated slots stay disabled across future passes until **Reactivate** is used.
- Added per-slot **Record Macro**, **Set rarity area**, **Test detection**, **Reactivate**, **Clear**, and live status controls.
- Added configurable **pre-check** and **final result scan** windows for safer rare protection.
- Sequence macros are stored independently in shared app data and survive app version updates/rollback.
- Retained the v15 **Low-Impact Game Engine**, Game Compatibility Mode, exact absolute-coordinate recording, input coalescing, CPU-saving scheduler, and click reliability fixes.
- Legacy single-macro mode remains available.

## v15.0.0 — Low-Impact Game Engine
Released: 2026-09-07

- Added **Game Compatibility Mode**, enabled by default, to reduce CPU/GPU/input overhead while Roblox is running.
- Reduced the detector from the old ~83 scans/sec default to about 33 scans/sec in compatibility mode and runs its worker at a lower Windows thread priority.
- Capped generated smooth/interpolated mouse movement at **120 Hz** in compatibility mode. Real recorded absolute mouse anchors are still preserved exactly.
- Re-enabled normal Windows movement-event coalescing in compatibility mode and avoids sending duplicate generated cursor positions.
- Reworked the precision scheduler so it sleeps for most of each wait instead of continuously yielding/spinning near every recorded mouse event. This substantially reduces unnecessary CPU contention with Roblox.
- Improved click reliability: if a cursor correction is needed, the engine now gives Roblox a configurable **hover settle** window before mouse-down, and very short recorded clicks receive a configurable **minimum click hold** time.
- Removed unnecessary per-loop work while replaying: fewer UI callbacks, fewer analytics/log refreshes, no per-loop trigger sound, and slower decorative animations while the macro is active.
- OpenCV now uses a single CPU thread and disables OpenCL for rarity detection, avoiding unnecessary thread/GPU contention for such a small screen crop.
- Added new performance controls in Settings for **Game Compatibility Mode**, **Hover settle**, **Minimum click hold**, and **Template scan frequency**.
- Existing recordings, absolute coordinates, SECRET/MYTHIC stop conditions, shared settings, analytics, and version rollback remain compatible.

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
