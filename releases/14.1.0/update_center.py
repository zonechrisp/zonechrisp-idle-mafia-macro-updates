import importlib.util
import os
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("IDLE_MAFIA_ROOT", str(THIS_DIR.parent.parent))).resolve()
BASE_FILE = ROOT / "versions" / "14.0.0" / "update_center.py"

if not BASE_FILE.exists():
    raise RuntimeError("The v14.0.0 Update Center base is missing.")

spec = importlib.util.spec_from_file_location("idle_mafia_update_center_base", BASE_FILE)
_base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_base)

UpdateController = _base.UpdateController
UpdateDialog = getattr(_base, "UpdateDialog", None)
pretty_version = getattr(_base, "pretty_version", lambda v: str(v))
