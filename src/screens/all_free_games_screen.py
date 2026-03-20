from .base_screen import BaseScreen


class AllGamesScreen(BaseScreen):
    def __init__(self):
        super().__init__("All", "This page lists all free-to-play games from every supported source.")
