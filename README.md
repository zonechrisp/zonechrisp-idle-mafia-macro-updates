# Roblox Auto Roll Selector — Update Feed

This repository is the public update feed used by the app's **Update Center**. The repository name is legacy from the original Idle Mafia-only versions; the current app is designed for Roblox roll/selection workflows more generally.

## Release channels

**Stable: v17.1.3 — Alpha Legacy Archive**

v17.1.3 adds the third Update Center channel and keeps the modern app as the normal Stable experience.

**Beta: modern preview/history**

Beta contains modern v14+ releases and continues to include Stable releases in the Update Center.

**Alpha: genuine historical v1–v13 builds**

Alpha is the pre-v14 legacy archive. Selecting a v1–v13 entry installs and opens that historical build as a **one-time legacy session**. It does not replace the selected Stable version; after closing the legacy build, reopening `RUN_APP.bat` returns to the modern Stable app.

The v1–v13 builds are stored in one shared legacy archive. The updater verifies its SHA-256 checksum, rejects unsafe archive paths/links/devices, and extracts only the selected version. Historical builds keep their original generation-specific behavior and dependencies.

- `manifest.json` declares Stable, Beta and Alpha releases.
- `packages/<version>/` contains Base64-chunked modern update packages.
- `packages/alpha-legacy-v1-v13/` contains the shared historical archive chunks.
- `CHANGELOG.md` contains the human-readable release history.

Modern update packages are concatenated, Base64-decoded and SHA-256 verified before installation. Modern versions remain side-by-side while current settings, macros, uploaded target images, Popup Recovery data and sequence data stay in shared app data.
