from PyQt6.QtCore import QThread, pyqtSignal
import requests
from html import escape
from sources import APIs
from .html import bad_response_html, free_to_play_games_html_page, error_html_page, not_found_html_page
import json
import os


class FreeToPlayGames(QThread):
    games = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

    def run(self):
        self.get_free_to_play_games()

    def _fast_thumbnail_url(self, url: str) -> str:
        cleaned = str(url or "").strip()
        if cleaned.startswith("https://www.freetogame.com/"):
            return "http://" + cleaned[len("https://"):]
        return cleaned

    def get_free_to_play_games(self):
        try:
            # fetch data
            response = requests.get(
                url=APIs.free_games, timeout=20, headers=self.headers)
            if response.status_code != 200:
                self.games.emit(bad_response_html.html(
                    reason=str(response.status_code)))
                return

            games = response.json()
            output = free_to_play_games_html_page.html
            for game in games:
                title = escape(str(game.get("title", "Unknown Title")))
                short_description = escape(
                    str(game.get("short_description", "")))
                genre = escape(str(game.get("genre", "N/A")))
                platform = escape(str(game.get("platform", "N/A")))
                publisher = escape(str(game.get("publisher", "N/A")))
                release_date = escape(str(game.get("release_date", "N/A")))
                thumbnail = escape(self._fast_thumbnail_url(
                    game.get("thumbnail", "")))
                game_url = escape(str(game.get("game_url", "#")))

                output += f"""
                <div class="card">
                    <img class="thumb" src="{thumbnail}" alt="{title}">
                    <div class="content">
                        <div class="title">{title}</div>
                        <div class="desc">{short_description}</div>
                        <div class="meta">
                            <b>Genre:</b> {genre}<br>
                            <b>Platform:</b> {platform}<br>
                            <b>Publisher:</b> {publisher}<br>
                            <b>Release:</b> {release_date}
                        </div>
                        <a class="btn" href="{game_url}">Play Now</a>
                    </div>
                </div>
                """

            output += """
            </div>
            </body>
            </html>
            """
            self.games.emit(output)
            
            # write data to ../data/free_to_play_games.json 
            os.makedirs("./data", exist_ok=True)
            with open("./data/free_to_play_games.json", "w") as file:
                json.dump(games, file, indent=4)
            return
        except Exception as e:
            self.games.emit(error_html_page.html(message=str(e)))



class SearchGame(QThread):
    game = pyqtSignal(str)
    
    def __init__(self, name: str = None):
        super().__init__()
        self.name = name.lower()
        
    def run(self):
        self.search()
        
    def _fast_thumbnail_url(self, url: str) -> str:
        cleaned = str(url or "").strip()
        if cleaned.startswith("https://www.freetogame.com/"):
            return "http://" + cleaned[len("https://"):]
        return cleaned
    
    def search(self):
        try:
            # read ../data/free_to_play_games.json
            if not os.path.exists("./data"):
                self.game.emit(error_html_page.html(message="./data directory is missing!"))
                return
            
            with open("./data/free_to_play_games.json", "r") as file:
                data = json.load(file)
            
            # search for game
            output = free_to_play_games_html_page.html
            for game in data:
                if self.name in game["title"].lower():
                    title = escape(str(game.get("title", "Unknown Title")))
                    short_description = escape(
                        str(game.get("short_description", "")))
                    genre = escape(str(game.get("genre", "N/A")))
                    platform = escape(str(game.get("platform", "N/A")))
                    publisher = escape(str(game.get("publisher", "N/A")))
                    release_date = escape(str(game.get("release_date", "N/A")))
                    thumbnail = escape(self._fast_thumbnail_url(
                        game.get("thumbnail", "")))
                    game_url = escape(str(game.get("game_url", "#")))

                    output += f"""
                    <div class="card">
                        <img class="thumb" src="{thumbnail}" alt="{title}">
                        <div class="content">
                            <div class="title">{title}</div>
                            <div class="desc">{short_description}</div>
                            <div class="meta">
                                <b>Genre:</b> {genre}<br>
                                <b>Platform:</b> {platform}<br>
                                <b>Publisher:</b> {publisher}<br>
                                <b>Release:</b> {release_date}
                            </div>
                            <a class="btn" href="{game_url}">Play Now</a>
                        </div>
                    </div>
                    """
                    self.game.emit(output)
                    return 
            self.game.emit(not_found_html_page.html)
            return
        except Exception as e:
            self.game.emit(error_html_page.html(message=str(e)))
            
            
            