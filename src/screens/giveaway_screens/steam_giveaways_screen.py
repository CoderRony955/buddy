from .base_screen import BaseScreen


class SteamScreen(BaseScreen):
    def __init__(self):
        super().__init__("Steam", "Free-to-play games available from Steam.")
