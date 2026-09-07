# Changelog

## v17.1.2 — Popup Recovery v3 & Runtime Audit
Released: 2026-09-07
Channel: Beta

- Fixed **Popup Recovery across all 10 Sequence slots**. Every slot now uses an isolated runtime context containing that slot’s popup image, popup area and recovery macro.
- Added slot-safe routing: if a popup belonging to Slot 7 is detected, Slot 7’s recovery macro runs even if another slot is about to start.
- Reworked the popup watcher for **short-lived dialogs**. It scans at a fast low-CPU cadence, can trigger immediately on a very strong single-frame match, and uses a short confirmation window for borderline matches.
- Improved popup matching accuracy by finding the dialog from grayscale structure first, then checking colour and text/edge detail at that **same matched location** instead of letting each channel match a different part of the screen.
- Precomputes scale-tolerant popup templates and skips expensive colour/edge checks on obvious non-matches, keeping detection responsive without bringing back the old Roblox lag problem.
- Added a **cross-slot safety sweep** before each sequence macro to catch delayed confirmation dialogs left behind by any configured slot.
- Popup Detection Test now samples a short burst of frames and reports the peak score, which is more representative for fast or animated popups than a single screenshot.
- Added a 10-slot Popup Recovery preflight at sequence start for missing files/configuration and display-layout mismatches in recorded recovery actions.
- Runtime audit completed: both Python files compile, the 10-slot popup configuration/matcher path was exercised with synthetic dialogs, slot-specific action routing was verified, and the release ZIP passed integrity testing.
- **Stable remains v16.2.0. v17.1.2 is Beta.**

## v17.1.1 — Purple UI & Scroll Stability
Released: 2026-09-07
Channel: Beta

- Fixed the scroll rendering/ghosting issue that could make cards and controls overlap or leave visual artifacts after scrolling up and down.
- Stopped recursively restyling `CTkScrollableFrame` internals, stabilized scroll-region updates, and temporarily reduces decorative redraws during active scrolling.
- Replaced the red branding with a new purple target-style app/taskbar logo and a purple visual system.
- Removed the Analytics page and simplified the sidebar/navigation.
- Refined the Automation Studio interface with cleaner cards, clearer page names, stronger hierarchy, and less visual clutter.
- Rebuilt **Help & Guide** with instructions for mouse + keyboard recording, Smart Vision custom targets, thresholds, scale tolerance, the 10-slot sequence, Popup Recovery, hotkeys, Game Compatibility Mode, updates, and troubleshooting.
- Reorganized release channels: **v16.2.0 is the only Stable release**. v17.1.1, all v17 releases, and all other historical releases are now in the **Beta** channel.
- Retained Smart Vision, Popup Recovery, keyboard recording, 10 sequence slots, per-slot target deactivation, and the low-impact Roblox playback engine.

## v17.1.0 — Smart Vision & Popup Recovery
Released: 2026-09-07
Channel: Beta

- Added per-slot Popup Recovery for confirmation dialogs and other interruptions.
- Added Smart Vision custom target recognition combining grayscale structure, colour appearance, and edge/text-shape detail.
- Added scale-tolerant custom image matching and configurable match threshold controls.
- Text in templates is matched visually; this is template recognition rather than semantic OCR.
- Retained 10 sequence slots, keyboard recording, and the low-impact engine.

## v17.0.0 — Universal Roblox Target Engine
Released: 2026-09-07
Channel: Beta

- Renamed the app to **Roblox Auto Roll Selector**.
- Added custom uploaded visual target templates for Roblox games.
- Added optional keyboard recording alongside mouse recording.
- Expanded Sequence Mode to 10 independent slots.

## v16.2.0 — In-App Recording Countdown
Released: 2026-09-07
Channel: Stable

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

- Added the in-app Update Center, SHA-256 verification, side-by-side versions, Stable/Beta channels, and rollback support.

## v13

- Added configurable SECRET / MYTHIC / BOTH stop conditions.
- Added precision playback and rare-detection improvements.
