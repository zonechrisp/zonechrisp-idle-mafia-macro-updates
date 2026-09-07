import base64
import ctypes
import importlib.util
import os
import sys
from io import BytesIO
from pathlib import Path

from PIL import Image
import customtkinter as ctk
import tkinter as tk

APP_VERSION = "14.1.0"
THIS_DIR = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("IDLE_MAFIA_ROOT", str(THIS_DIR.parent.parent))).resolve()
BASE_DIR = ROOT / "versions" / "14.0.0"
ICON_B64_PATH = THIS_DIR / "app_icon.b64"


def _set_app_id():
    if sys.platform == "win32":
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("zonechrisp.idlemafia.precisionmacro")
        except Exception:
            pass


def _load_base():
    base_main = BASE_DIR / "main.py"
    if not base_main.exists():
        raise RuntimeError("v14.1 requires the installed v14.0.0 base. Use Update Center to reinstall v14.0.0, then install v14.1.0 again.")
    if str(THIS_DIR) not in sys.path:
        sys.path.insert(0, str(THIS_DIR))
    if str(BASE_DIR) not in sys.path:
        sys.path.insert(1, str(BASE_DIR))
    spec = importlib.util.spec_from_file_location("idle_mafia_v14_base", base_main)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _all_widgets(widget):
    for child in widget.winfo_children():
        yield child
        yield from _all_widgets(child)


def _apply_icon(app):
    try:
        b64 = ICON_B64_PATH.read_text(encoding="ascii").strip()
        app._v141_icon_photo = tk.PhotoImage(data=b64)
        app.iconphoto(True, app._v141_icon_photo)
        app.wm_iconphoto(True, app._v141_icon_photo)
        pil = Image.open(BytesIO(base64.b64decode(b64))).convert("RGBA")
        app._v141_brand_image = ctk.CTkImage(light_image=pil, dark_image=pil, size=(42, 42))
        for widget in _all_widgets(app):
            if isinstance(widget, ctk.CTkLabel):
                try:
                    if str(widget.cget("text")) == "IM":
                        widget.configure(text="", image=app._v141_brand_image, fg_color="transparent")
                        break
                except Exception:
                    pass
    except Exception:
        pass


def main():
    _set_app_id()
    base = _load_base()
    app = base.IdleMafiaMacroApp()
    app.title(f"Idle Mafia • Precision Mouse Macro v{APP_VERSION}")
    _apply_icon(app)
    app.mainloop()


if __name__ == "__main__":
    main()
