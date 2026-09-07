# Changelog

## v17.1.3 — Alpha Legacy Archive
Released: 2026-09-08
Channel: Stable

- Added **Alpha** as a third Update Center channel.
- Added the genuine archived **v1–v13** builds as selectable historical releases.
- Alpha builds install and open as one-time legacy sessions without replacing the selected Stable version.
- Added SHA-256 verification for the shared legacy archive and safe selective extraction that rejects path traversal, links and device entries.
- Stable and Beta continue using the modern side-by-side update system and shared app data.

## v17.1.2 — Popup Recovery v3 & Runtime Audit
Released: 2026-09-07
Channel: Stable

- Fixed **Popup Recovery across all 10 Sequence slots**. Every slot now uses an isolated runtime context containing that slot’s popup image, popup area and recovery macro.
- Added slot-safe routing: if a popup belonging to Slot 7 is detected, Slot 7’s recovery macro runs even if another slot is about to start.
- Reworked the popup watcher for **short-lived dialogs** with faster low-CPU scanning and strong single-frame triggering.
- Improved popup matching by evaluating structure, colour and text/edge evidence at the same matched location.
- Added a cross-slot safety sweep, popup preflight checks and burst-based detection testing.
- Completed a runtime/package audit and promoted v17.1.2 to Stable.

## v17.1.1 — Purple UI & Scroll Stability
Released: 2026-09-07
Channel: Beta

- Fixed the scroll rendering/ghosting issue that could make cards and controls overlap or leave visual artifacts after scrolling.
- Stopped recursively restyling `CTkScrollableFrame` internals and stabilized scroll-region updates.
- Replaced the red branding with a purple target-style app/taskbar logo and visual system.
- Removed Analytics, simplified navigation and rebuilt Help & Guide.
- Retained Smart Vision, Popup Recovery, keyboard recording, 10 sequence slots, per-slot target deactivation and the low-impact Roblox playback engine.

## v17.1.0 — Smart Vision & Popup Recovery
Released: 2026-09-07
Channel: Beta

- Added per-slot Popup Recovery for confirmation dialogs and other interruptions.
- Added Smart Vision custom target recognition combining grayscale structure, colour appearance and edge/text-shape detail.
- Added scale-tolerant custom image matching and configurable match threshold controls.
- Retained 10 sequence slots, keyboard recording and the low-impact engine.

## v17.0.0 — Universal Roblox Target Engine
Released: 2026-09-07
Channel: Beta

- Renamed the app to **Roblox Auto Roll Selector**.
- Added custom uploaded visual target templates for Roblox games.
- Added optional keyboard recording alongside mouse recording.
- Expanded Sequence Mode to 10 independent slots.

## v16.2.0 — In-App Recording Countdown
Released: 2026-09-07
Channel: Beta

- The app stays visible while a macro recording countdown is running.
- Engine status shows the countdown directly and changes to **RECORDING** only when capture is live.
- Removed the problematic floating countdown overlay.

## v16.0.0 — Five-Slot Sequence Engine
Released: 2026-09-07
Channel: Beta

- Added Sequence Mode with independent macro + rarity-area pairs.
- A detected target disables only its own slot while the remaining sequence continues.

## v15.0.0 — Low-Impact Game Engine
Released: 2026-09-07
Channel: Beta

- Added Game Compatibility Mode and reduced CPU/GPU/input overhead while Roblox is running.
- Improved click reliability and reduced detector/input scheduling load.

## v14.1.1 — Windows Taskbar Icon Fix
Released: 2026-09-07
Channel: Beta

- Fixed Windows taskbar icon handling.

## v14.1.0 — App Icon Micro Update
Released: 2026-09-07
Channel: Beta

- Added custom app branding.

## v14.0.0 — Update Center
Released: 2026-09-07
Channel: Beta

- Added the in-app Update Center, SHA-256 verification, side-by-side versions, Stable/Beta channels and rollback support.

## Alpha legacy archive — v1–v13

These historical builds now appear individually in the **Alpha** channel.

- **v13 — Selectable Rare Stop & Smooth Engine:** selectable BOTH, SECRET-only or MYTHIC-only stopping plus smoother precision playback.
- **v12 — Precision Mouse Recorder:** direct precision mouse recording and low-level Windows playback.
- **v11 — Dark Dashboard & Analytics:** introduced the dark multi-page dashboard and analytics/activity logging.
- **v10 — Automatic Python Setup:** added automatic Python setup while retaining the Razer Play Once controller.
- **v9 — Razer Play Once Controller:** switched from toggle control to one-shot Synapse playback decisions.
- **v8 — Razer Synapse Rare-Stop Toggle:** dedicated SECRET/MYTHIC detector that stops a Synapse toggle macro.
- **v7 — Recorded Mouse Macro:** added real mouse movement/click recording with background rarity detection.
- **v6 — Low-Level Click Guard:** added smooth low-level clicking, cursor verification and a visual button guard.
- **v5 — Confirm Flow & Roblox Hover Fix:** added Roll → Dismiss → Confirm flow and Roblox hover-state handling.
- **v4 — Dismiss Flow & Global Hotkeys:** added the Dismiss flow plus global F6/F7 controls.
- **v3 — Normal Roll Macro:** moved rolling into the app instead of relying on an in-game Auto Roll button.
- **v2 — Safer Rare Stop:** tuned SECRET/MYTHIC detection and consecutive-frame confirmation.
- **v1 — Auto-Roll Watcher:** original screen watcher with colour/template rare detection and pre-roll safety checks.
