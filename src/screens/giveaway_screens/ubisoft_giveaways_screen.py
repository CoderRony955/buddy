from .base_screen import BaseScreen
from .base_screen import BaseScreen
from .base_screen import BaseScreen
from .base_screen import BaseScreen
from PyQt6.QtWidgets import QPushButton, QToolBar, QLabel, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QFont, QDesktopServices, QWheelEvent, QKeyEvent
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from datetime import datetime
import qtawesome as qta
import webbrowser
import style
import os

# dialog
from .dialogs import SaveToDBDialog

# threads
from ...fetchers import giveaways


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



class UbisoftScreen(BaseScreen):
    def __init__(self):
        super().__init__("Ubisoft", "Free Gaming Stuffs Giveaways from Ubisoft.")
        
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
        self.db_save_action.triggered.connect(self.open_save_to_db_dialog)

        # label to display giveaway fetch date
        self.date_label = QLabel()
        self.date_label.setText("Giveaway Date will be displayed here ⌛")
        self.date_label.setFont(QFont("monospace", 10))
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_label.setFixedSize(250, 36)
        self.date_label.setStyleSheet(
            "border-radius: 16px; background: #141414; color: white; border: 1px solid #30363d;")
        
        # refresh button
        fetch_giveaways_btn = QPushButton()
        fetch_giveaways_btn.setIcon(
            QIcon(qta.icon("fa5s.sync", style="white")))
        fetch_giveaways_btn.setToolTip("refersh & fetch all")
        fetch_giveaways_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        fetch_giveaways_btn.setFixedSize(40, 36)
        fetch_giveaways_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #03331f;} QPushButton:hover {background: #045231;}")
        fetch_giveaways_btn.clicked.connect(self.fetchAllGiveaways)

        # games giveaways fetch button
        game_giveaways_fetch_btn = QPushButton()
        game_giveaways_fetch_btn.setIcon(QIcon(qta.icon("fa5s.gamepad", style="white")))
        game_giveaways_fetch_btn.setToolTip("fetch latest games givewaways")
        game_giveaways_fetch_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        game_giveaways_fetch_btn.setFixedSize(40, 36)
        game_giveaways_fetch_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #03081c;} QPushButton:hover {background: #041145;}")
        game_giveaways_fetch_btn.clicked.connect(self.fetchGamesGiveaways)

        # gaming loot givewaways fetch button
        gaming_loot_giveaways_fetch_btn = QPushButton()
        gaming_loot_giveaways_fetch_btn.setIcon(QIcon(qta.icon("fa5s.box-open", style="white")))
        gaming_loot_giveaways_fetch_btn.setToolTip("fetch latest gaming loot giveaways")
        gaming_loot_giveaways_fetch_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        gaming_loot_giveaways_fetch_btn.setFixedSize(40, 36)
        gaming_loot_giveaways_fetch_btn.setStyleSheet(
            "QPushButton {border-radius: 15px; background: #0f00e0;} QPushButton:hover {background: #0c0661;}")
        gaming_loot_giveaways_fetch_btn.clicked.connect(self.fetchLootsGiveaways)


        # display area
        self.display_area = CustomWebEngineView()
        self.display_area.setPage(CustomWebEnginePage(self.display_area))
        self.display_area.setZoomFactor(1.0)
        self.display_area.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        settings = self.display_area.settings()
        settings.setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True
        )
        settings.setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True
        )
        from .html import giveaways_default_screen_html
        self.display_area.setHtml(
            giveaways_default_screen_html.html("https://upload.wikimedia.org/wikipedia/commons/4/44/Cib-ubisoft_%28CoreUI_Icons_v1.0.0%29.svg", "Ubisoft")
        )

        hlayout.addWidget(self.date_label)
        hlayout.addWidget(fetch_giveaways_btn)
        hlayout.addWidget(game_giveaways_fetch_btn)
        hlayout.addWidget(gaming_loot_giveaways_fetch_btn)

        layout.insertWidget(0, toolbar)
        layout.insertLayout(3, hlayout)
        layout.insertWidget(4, self.display_area)
    
    # Fetch Giveaways
    # to fetch both games and loots
    def fetchAllGiveaways(self):
        from .html import loading_screen
        self.display_area.setHtml(loading_screen.html)
        self.fetcher = giveaways.GamesAndLoots(platform="ubisoft", cache_data_path="./data/ubisoft_giveaways.json")
        self.fetcher.giveaways.connect(self.display_giveaways)
        self.fetcher.start()
    
    # to fetch games only
    def fetchGamesGiveaways(self):
        from .html import loading_screen
        self.display_area.setHtml(loading_screen.html)
        self.fetcher = giveaways.GamesAndLoots(platform="ubisoft", loots=False, cache_data_path="./data/ubisoft_giveaways.json")
        self.fetcher.giveaways.connect(self.display_giveaways)
        self.fetcher.start()
        
    # to fetch loots only
    def fetchLootsGiveaways(self):
        from .html import loading_screen
        self.display_area.setHtml(loading_screen.html)
        self.fetcher = giveaways.GamesAndLoots(platform="ubisoft", games=False, cache_data_path="./data/ubisoft_giveaways.json")
        self.fetcher.giveaways.connect(self.display_giveaways)
        self.fetcher.start()
    
    def display_giveaways(self, giveaways):
        self.display_area.setHtml(giveaways)
        date_and_time = f"{datetime.now().ctime()}"
        self.date_label.setText(date_and_time)
    
    def open_save_to_db_dialog(self):
        from ...cache_data_files import ubisoft_gaming_stuffs_giveaways
        if not os.path.exists(ubisoft_gaming_stuffs_giveaways):
            # check ./data dir if not exist then create one
            os.makedirs("./data", exist_ok=True)
            # create ./data/ubisoft_giveaways.json file
            with open("./data/ubisoft_giveaways.json", "w") as file:
                file.write("[]")
                
            # informational message box
            title = "Data cache file empty!"
            message = "newly ./data/ubisoft_giveaways.json just created because, data cache not found! So, please refetch data then try again to insert data into Database."
            informational = QMessageBox()
            informational.setWindowTitle(title)
            informational.setText(message)
            informational.setIcon(QMessageBox.Icon.Information)
            informational.setStandardButtons(QMessageBox.StandardButton.Ok)
            informational.exec()
            return
        
        db_dialog = SaveToDBDialog.DBDialog(ubisoft_gaming_stuffs_giveaways)
        db_dialog.exec()
