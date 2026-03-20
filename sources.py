class APIs:
    free_games = "https://www.freetogame.com/api/games"

    # games giveaways different endpoints to getting different data category wise
    all_giveaways = "https://gamerpower.com/api/giveaways"
    android_games_giveaways = "https://www.gamerpower.com/api/giveaways?platform=android"
    ios_games_giveaways = "https://www.gamerpower.com/api/giveaways?platform=android"
    epic_games_giveaways = "https://www.gamerpower.com/api/giveaways?platform=epic-games-store"
    steam_giveaways = "https://www.gamerpower.com/api/giveaways?platform=steam"
    gog_giveaways = "https://www.gamerpower.com/api/giveaways?platform=gog"
    ubisoft_giveaways = "https://www.gamerpower.com/api/giveaways?platform=ubisoft"
    ps_giveaways = "https://www.gamerpower.com/api/giveaways?platform=ps5"
    xbox_giveaways = "https://www.gamerpower.com/api/giveaways?platform=xbox-series-xs"
    switch_giveaways = "https://www.gamerpower.com/api/giveaways?platform=switch"

    @staticmethod
    def free_games_by_category(category: str):
        return f"https://www.freetogame.com/api/games?category={category}"
