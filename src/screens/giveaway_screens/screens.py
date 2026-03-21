from .all_free_games_screen import AllGamesScreen
from .epic_games_giveaways_screen import EpicGamesScreen
from .steam_giveaways_screen import SteamScreen
from .ubisoft_giveaways_screen import UbisoftScreen
from .android_games_giveaways_screen import AndroidScreen
from .xbox_stuff_giveaways_screen import XboxScreen
from .switch_games_stuff_giveaways_screen import SwitchScreen
from .battlenet_games_giveaways_screen import BattlenetScreen
from .ps_stuff_giveaways_screen import PlayStationScreen
from .ios_games_stuff_giveaways_screen import IOSScreen
from .ai_bot_chat_screen import AIChatbotScreen


class Screen:
    all_games = AllGamesScreen
    epic_games = EpicGamesScreen
    steam = SteamScreen
    ubisoft = UbisoftScreen
    android = AndroidScreen
    ios = IOSScreen
    xbox = XboxScreen
    switch = SwitchScreen
    playstation = PlayStationScreen
    battlenet = BattlenetScreen
    ai_chat = AIChatbotScreen
