class APIs:
    free_games = "https://www.freetogame.com/api/games"

    # games giveaways different endpoints to getting different data category wise
    for_giveaways_by_platform = lambda platform: f"https://www.gamerpower.com/api/giveaways?platform={platform}"
    for_free_gaming_stuffs_giveaways = lambda platform, type: f"https://www.gamerpower.com/api/giveaways?platform={platform}&type={type}"
 