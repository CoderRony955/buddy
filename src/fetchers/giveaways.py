from PyQt6.QtCore import QThread, pyqtSignal
import requests
from html import escape
from sources import APIs
from .html import bad_response_html, error_html_page, not_found_html_page, giveaways_not_found_screen_html
import json
import os


class GamesAndLoots(QThread):
    giveaways = pyqtSignal(str)

    def __init__(self, platform: str = None, games: bool = True, loots: bool = True, cache_data_path: str = None):
        super().__init__()
        self.platform = (platform or "").strip()
        self.games = bool(games)
        self.loots = bool(loots)
        self.cache_data_path = cache_data_path
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }

    def run(self):
        if not self.games:
            self.fetchLoots()
        elif not self.loots:
            self.fetchGames()
        else:
            self.fetchAll()

    def _build_header_html(self, count: int) -> str:
        platform_label = escape(self.platform.title()
                                ) if self.platform else "All Platforms"
        feed_label = "Games + Loots"
        if self.games and not self.loots:
            feed_label = "Games"
        elif self.loots and not self.games:
            feed_label = "Loots"

        return f"""
        <div class="hero">
            <h2>Live Giveaways</h2>
            <p>{platform_label} • {feed_label} • {count} results</p>
        </div>
        """

    def _normalize_instructions(self, instructions: str) -> str:
        text = str(instructions or "").strip()
        if not text:
            return "<li>Open the giveaway page and follow the claim steps.</li>"

        lines = [line.strip() for line in text.replace(
            "\r", "").split("\n") if line.strip()]
        cleaned_lines = []
        for line in lines:
            if ". " in line and line.split(". ", 1)[0].isdigit():
                cleaned_lines.append(line.split(". ", 1)[1].strip())
            else:
                cleaned_lines.append(line)
        return "".join(f"<li>{escape(line)}</li>" for line in cleaned_lines)

    def _build_card_html(self, item: dict) -> str:
        title = escape(str(item.get("title", "Unknown Giveaway")))
        worth = escape(str(item.get("worth", "N/A")))
        image = escape(str(item.get("image") or item.get("thumbnail") or ""))
        description = escape(
            str(item.get("description", "No description available.")))
        platforms = escape(str(item.get("platforms", "N/A")))
        giveaway_type = escape(str(item.get("type", "N/A")))
        end_date = escape(str(item.get("end_date", "N/A")))
        published_date = escape(str(item.get("published_date", "N/A")))
        status = escape(str(item.get("status", "Unknown")))
        users = escape(str(item.get("users", "0")))
        open_url = escape(str(item.get("open_giveaway")
                          or item.get("open_giveaway_url") or "#"))
        source_url = escape(str(item.get("gamerpower_url", "#")))
        instructions_html = self._normalize_instructions(
            item.get("instructions", ""))

        return f"""
        <article class="card">
            <img class="thumb" src="{image}" alt="{title}">
            <div class="content">
                <div class="title">{title}</div>
                <div class="worth">{worth}</div>
                <div class="desc">{description}</div>

                <div class="meta-grid">
                    <div><b>Type:</b> {giveaway_type}</div>
                    <div><b>Status:</b> {status}</div>
                    <div><b>Platform:</b> {platforms}</div>
                    <div><b>Users:</b> {users}</div>
                    <div><b>Published:</b> {published_date}</div>
                    <div><b>Ends:</b> {end_date}</div>
                </div>

                <div class="steps-title">How to claim</div>
                <ol class="steps">
                    {instructions_html}
                </ol>

                <div class="actions">
                    <a class="btn btn-primary" href="{open_url}">Open Giveaway</a>
                    <a class="btn btn-ghost" href="{source_url}">Source</a>
                </div>
            </div>
        </article>
        """

    def _build_page_html(self, data: list[dict]) -> str:
        cards = "".join(self._build_card_html(item) for item in data)
        header = self._build_header_html(len(data))
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<style>
    * {{
        box-sizing: border-box;
    }}
    html, body {{
        margin: 0;
        padding: 0;
    }}
    body {{
        padding: 12px;
        font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        background: #0b1220;
        color: #eaf2ff;
        overflow-x: hidden;
    }}
    .hero {{
        background: #15243a;
        border: 1px solid #27466c;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 12px;
    }}
    .hero h2 {{
        margin: 0 0 4px 0;
        font-size: 20px;
        color: #ffffff;
    }}
    .hero p {{
        margin: 0;
        font-size: 12px;
        color: #bdd2ed;
    }}
    .container {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 12px;
        width: 100%;
    }}
    .card {{
        background: #121d2f;
        border: 1px solid #2a486f;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 8px 18px rgba(0, 0, 0, 0.3);
    }}
    .thumb {{
        width: 100%;
        aspect-ratio: 16 / 9;
        object-fit: cover;
        background: #0f1726;
        border-bottom: 1px solid #28466b;
    }}
    .content {{
        padding: 10px;
    }}
    .title {{
        font-size: 17px;
        font-weight: 700;
        color: #f2f7ff;
        margin-bottom: 6px;
        line-height: 1.3;
    }}
    .worth {{
        display: inline-block;
        background: #1a5f41;
        color: #d8ffe7;
        border: 1px solid #2f8a61;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 8px;
        margin-bottom: 8px;
    }}
    .desc {{
        font-size: 12px;
        color: #c9dbf2;
        line-height: 1.45;
        margin-bottom: 8px;
    }}
    .meta-grid {{
        display: grid;
        grid-template-columns: 1fr;
        gap: 4px;
        font-size: 11px;
        color: #aecded;
        margin-bottom: 8px;
    }}
    .meta-grid b {{
        color: #e3efff;
    }}
    .steps-title {{
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.2px;
        color: #e6f1ff;
        margin-bottom: 4px;
    }}
    .steps {{
        margin: 0 0 10px 18px;
        padding: 0;
        font-size: 11px;
        line-height: 1.45;
        color: #c8dbf3;
    }}
    .steps li {{
        margin-bottom: 3px;
    }}
    .actions {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    }}
    .btn {{
        display: inline-block;
        text-decoration: none;
        font-size: 11px;
        font-weight: 700;
        border-radius: 7px;
        padding: 7px 10px;
        border: 1px solid transparent;
    }}
    .btn-primary {{
        background: #24cf87;
        color: #072218;
    }}
    .btn-primary:hover {{
        background: #31e89b;
    }}
    .btn-ghost {{
        background: transparent;
        color: #d7e7ff;
        border-color: #406895;
    }}
    .btn-ghost:hover {{
        background: #1c2c44;
    }}
    @media (max-width: 640px) {{
        body {{
            padding: 8px;
        }}
        .container {{
            grid-template-columns: 1fr;
            gap: 10px;
        }}
        .title {{
            font-size: 16px;
        }}
    }}
</style>
</head>
<body>
    {header}
    <section class="container">
        {cards}
    </section>
</body>
</html>
"""

    def _cache_giveaways(self, data: list[dict]):
        os.makedirs("./data", exist_ok=True)
        with open(self.cache_data_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def fetchAll(self):
        try:
            response = requests.get(
                url=APIs.for_giveaways_by_platform(self.platform),
                timeout=20,
                headers=self.headers,
            )
            if response.status_code not in (200, 201):
                self.giveaways.emit(not_found_html_page.html(
                    reason=str(response.status_code)))
                return

            data = response.json()
            if not isinstance(data, list) or not data:
                self.giveaways.emit(giveaways_not_found_screen_html.html)
                return

            output = self._build_page_html(data)
            self.giveaways.emit(output)
            self._cache_giveaways(data)
        except Exception as e:
            self.giveaways.emit(error_html_page.html(message=str(e)))

    def fetchGames(self):
        try:
            response = requests.get(
                url=APIs.for_free_gaming_stuffs_giveaways(
                    self.platform, "game"),
                timeout=20,
                headers=self.headers,
            )
            if response.status_code not in (200, 201):
                self.giveaways.emit(bad_response_html.html(
                    reason=str(response.status_code)))
                return

            data = response.json()
            if not isinstance(data, list) or not data:
                self.giveaways.emit(giveaways_not_found_screen_html.html)
                return

            output = self._build_page_html(data)
            self.giveaways.emit(output)
            self._cache_giveaways(data)
        except Exception as e:
            self.giveaways.emit(error_html_page.html(message=str(e)))

    def fetchLoots(self):
        try:
            response = requests.get(
                url=APIs.for_free_gaming_stuffs_giveaways(
                    self.platform, "loot"),
                timeout=20,
                headers=self.headers,
            )
            if response.status_code not in (200, 201):
                self.giveaways.emit(bad_response_html.html(
                    reason=str(response.status_code)))
                return

            data = response.json()
            if not isinstance(data, list) or not data:
                self.giveaways.emit(giveaways_not_found_screen_html.html)
                return

            output = self._build_page_html(data)
            self.giveaways.emit(output)
            self._cache_giveaways(data)
        except Exception as e:
            self.giveaways.emit(error_html_page.html(message=str(e)))
