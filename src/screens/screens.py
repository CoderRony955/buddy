from .all_free_games_screen import AllGamesScreen
from .epic_games_giveaways_screen import EpicGamesScreen
from .search_screen import SearchScreen
from .steam_giveaways_screen import SteamScreen
from .ubisoft_giveaways_screen import UbisoftScreen
from .android_games_giveaways_screen import AndroidScreen
from .xbox_stuff_giveaways_screen import XboxScreen


class Screen:
    search = SearchScreen
    all_games = AllGamesScreen
    epic_games = EpicGamesScreen
    steam = SteamScreen
    ubisoft = UbisoftScreen
    android = AndroidScreen
    xbox = XboxScreen
