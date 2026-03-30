import sys
from pathlib import Path

from PyQt6.QtGui import QIcon


def resource_path(*parts: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parents[1]
    return str(base_path.joinpath(*parts))


def app_window_icon() -> QIcon:
    return QIcon(resource_path("icons", "buddy_logo.ico"))
