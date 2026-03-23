from .base_screen import BaseScreen
from PyQt6.QtWidgets import QPushButton, QToolBar, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QAction, QIcon, QFont, QDesktopServices, QWheelEvent, QKeyEvent
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from pathlib import Path
import base64
import qtawesome as qta
import webbrowser
import style

# threads 
from ...fetchers import free_to_play_games


class CustomWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationType.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url)  # 🔥 open in default browser
            return False  # prevent loading inside QWebEngineView
        return True


class CustomWebEngineView(QWebEngineView):
    def wheelEvent(self, event: QWheelEvent):
        # Keep zoom fixed even when user uses Ctrl + mouse wheel.
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            event.ignore()
            return
        super().wheelEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            if event.key() in (
                Qt.Key.Key_Plus,
                Qt.Key.Key_Equal,
                Qt.Key.Key_Minus,
                Qt.Key.Key_0,
            ):
                event.ignore()
                return
        super().keyPressEvent(event)


class AllGamesScreen(BaseScreen):
    def __init__(self):
        super().__init__(
            "Free-to-play Video Games",
            "This page lists all free-to-play games from every supported source.",
        )
        layout = self.layout()
        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(8)
        hlayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # toolbar
        toolbar = QToolBar()
        toolbar.setFixedHeight(40)
        toolbar.setObjectName("toolbar")
        toolbar.setMovable(False)
        toolbar.setStyleSheet(style.styling.toolbar)

        # github repository link
        self.github_repo = QAction()
        self.github_repo.setToolTip("visit github repository")
        self.github_repo.setIcon(QIcon(qta.icon("fa5b.github", style="black")))
        self.github_repo.triggered.connect(
            lambda: webbrowser.open("https://github.com/CoderRony955/buddy"))
        toolbar.addAction(self.github_repo)

        # a option to save data into mongodb (if user want)
        self.db_save_action = QAction()
        self.db_save_action.setToolTip("save data")
        self.db_save_action.setIcon(
            QIcon(qta.icon("fa5s.database", style="white")))
        toolbar.addAction(self.db_save_action)

        # search bar for searching any one specefic video game (free to play only from source)
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search for Free-to-play Game")
        self.search_bar.setFont(QFont("monospace", 10))
        self.search_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.search_bar.setFixedSize(250, 36)
        self.search_bar.setStyleSheet(
            "border-radius: 16px; background: #141414; color: white;")

        # search button
        search_btn = QPushButton()
        search_btn.setIcon(QIcon(qta.icon("fa5s.search", style="white")))
        search_btn.setToolTip("search game")
        search_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        search_btn.setFixedSize(40, 36)
        search_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #03081c;} QPushButton:hover {background: #041145;}")
        search_btn.clicked.connect(self.search_free_to_play_games)

        # fetch button
        fetch_btn = QPushButton()
        fetch_btn.setIcon(QIcon(qta.icon("fa5s.gamepad", style="white")))
        fetch_btn.setToolTip("fetch free-to-play games")
        fetch_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        fetch_btn.setFixedSize(40, 36)
        fetch_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #0f00e0;} QPushButton:hover {background: #0c0661;}")
        fetch_btn.clicked.connect(self.fetch_free_to_play_games)

        # refresh button
        refresh_btn = QPushButton()
        refresh_btn.setIcon(
            QIcon(qta.icon("fa5s.sync", style="white")))
        refresh_btn.setToolTip("refersh")
        refresh_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        refresh_btn.setFixedSize(40, 36)
        refresh_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #03331f;} QPushButton:hover {background: #045231;}")
        refresh_btn.clicked.connect(self.fetch_free_to_play_games)

        # display area
        self.display_area = CustomWebEngineView()
        self.display_area.setPage(CustomWebEnginePage(self.display_area))
        self.display_area.setZoomFactor(1.0)
        settings = self.display_area.settings()
        settings.setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True
        )
        settings.setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True
        )
        image_file = Path(__file__).resolve().parent / \
            "images" / "free_video_games.png"
        if image_file.exists():
            encoded = base64.b64encode(image_file.read_bytes()).decode("ascii")
            image_path = f"data:image/png;base64,{encoded}"
        else:
            image_path = QUrl.fromLocalFile(str(image_file)).toString()
        from .html import default_display_screen_html
        self.display_area.setHtml(
            default_display_screen_html.html(image_path),
            QUrl.fromLocalFile(str(image_file.parent) + "/"),
        )

        hlayout.addWidget(self.search_bar)
        hlayout.addWidget(search_btn)
        hlayout.addWidget(fetch_btn)
        hlayout.addWidget(refresh_btn)

        layout.insertWidget(0, toolbar)
        layout.insertLayout(3, hlayout)
        layout.insertWidget(4, self.display_area)

    def fetch_free_to_play_games(self):
        from .html import loading_screen
        self.display_area.setHtml(loading_screen.html)
        self.fetcher = free_to_play_games.FreeToPlayGames()
        self.fetcher.games.connect(self.display_games)
        self.fetcher.start()

    def display_games(self, games):
        self.display_area.setHtml(games)
        
        
    def search_free_to_play_games(self):
        from .html import loading_screen
        game_name = self.search_bar.text()
        self.display_area.setHtml(loading_screen.html)
        self.search = free_to_play_games.SearchGame(name=game_name)
        self.search.game.connect(self.display_game)
        self.search.start()

    def display_game(self, game):
        self.display_area.setHtml(game)

    def open_external_link(self, url: QUrl):
        target = QUrl(url)
        if target.scheme() == "":
            target = QUrl(f"https://{target.toString().lstrip('/')}")
        QDesktopServices.openUrl(target)
