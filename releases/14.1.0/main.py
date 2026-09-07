import ctypes
import importlib.util
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageTk
import customtkinter as ctk

APP_VERSION = "14.1.0"
THIS_DIR = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("IDLE_MAFIA_ROOT", str(THIS_DIR.parent.parent))).resolve()
BASE_DIR = ROOT / "versions" / "14.0.0"


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


def _make_icon():
    s = 128
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((4, 4, 124, 124), radius=27, fill=(15, 18, 21, 255), outline=(255, 65, 65, 255), width=4)
    d.rounded_rectangle((9, 9, 119, 119), radius=23, outline=(110, 20, 24, 180), width=2)
    d.ellipse((33, 23, 95, 49), fill=(20, 22, 25, 255))
    d.polygon([(43, 36), (49, 17), (79, 17), (88, 37)], fill=(24, 26, 29, 255))
    d.rectangle((48, 30, 84, 35), fill=(240, 45, 52, 255))
    d.polygon([(47, 48), (81, 48), (94, 72), (77, 74), (64, 58), (50, 74), (33, 72)], fill=(10, 12, 14, 255))
    red = (238, 42, 49, 255)
    d.polygon([(24, 65), (43, 65), (64, 85), (85, 65), (104, 65), (104, 107), (88, 107), (88, 84), (64, 106), (40, 84), (40, 107), (24, 107)], fill=red)
    d.ellipse((48, 72, 80, 104), outline=(255, 77, 77, 255), width=4)
    for xy in [((64, 66), (64, 75)), ((64, 101), (64, 111)), ((42, 88), (51, 88)), ((77, 88), (87, 88))]:
        d.line(xy, fill=(255, 87, 87, 255), width=4)
    d.polygon([(58, 78), (58, 99), (64, 94), (70, 104), (75, 101), (69, 91), (78, 90)], fill=(245, 247, 249, 255), outline=(180, 185, 190, 255))
    return img


def _apply_icon(app):
    try:
        pil = _make_icon()
        app._v141_icon_photo = ImageTk.PhotoImage(pil.resize((64, 64), Image.Resampling.LANCZOS))
        app.iconphoto(True, app._v141_icon_photo)
        app.wm_iconphoto(True, app._v141_icon_photo)
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
