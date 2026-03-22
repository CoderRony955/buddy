from .base_screen import BaseScreen
from PyQt6.QtWidgets import QPushButton, QLabel, QTextBrowser, QToolBar, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QAction, QIcon, QFont
from pathlib import Path
import qtawesome as qta
import webbrowser
import style


class AllGamesScreen(BaseScreen):
    def __init__(self):
        super().__init__(
            "Free-to-play Video Games",
            "This page lists all free-to-play games from every supported source.",
        )
        layout = self.layout()
        hlayout = QHBoxLayout()
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(10)
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
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search for Free-to-play Game")
        search_bar.setFont(QFont("monospace", 10))
        search_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        search_bar.setFixedSize(250, 36)
        search_bar.setStyleSheet(
            "border-radius: 16px; background: #141414; color: white;")

        # search button
        search_btn = QPushButton()
        search_btn.setIcon(QIcon(qta.icon("fa5s.search", style="white")))
        search_btn.setToolTip("search game")
        search_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        search_btn.setFixedSize(40, 36)
        search_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #03081c;} QPushButton:hover {background: #041145;}")

        # refresh button
        refresh_btn = QPushButton()
        refresh_btn.setIcon(
            QIcon(qta.icon("fa5s.sync", style="black")))
        refresh_btn.setToolTip("refersh")
        refresh_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        refresh_btn.setFixedSize(40, 36)
        refresh_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #17e8b7;} QPushButton:hover {background: #7df0d5;}")

        # display area
        display_area = QTextBrowser()
        image_file = Path(__file__).resolve().parent / \
            "images" / "free_video_games.png"
        image_path = QUrl.fromLocalFile(str(image_file)).toString()
        from .html import default_display_screen_html
        display_area.setHtml(default_display_screen_html.html(image_path))

        hlayout.addWidget(search_bar)
        hlayout.addWidget(search_btn)
        hlayout.addWidget(refresh_btn)

        layout.insertWidget(0, toolbar)
        layout.insertLayout(3, hlayout)
        layout.insertWidget(4, display_area)
