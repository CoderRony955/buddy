class APIs:
    free_games = "https://www.freetogame.com/api/games"

    # games giveaways different endpoints to getting different data category wise
    all_giveaways = "https://gamerpower.com/api/giveaways"

    @staticmethod
    def for_free_gaming_stuff_giveaways(platform: str, type: str):
        return f"https://www.gamerpower.com/api/giveaways?platform={platform}&type={type}"

    @staticmethod
    def for_free_games_by_category(category: str):
        return f"https://www.freetogame.com/api/games?category={category}"
