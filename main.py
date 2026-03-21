import sys

from PyQt6.QtCore import QEasingCurve, QParallelAnimationGroup, QPropertyAnimation, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QFont, QIcon, QCursor
from PyQt6.QtCore import QSize, Qt
from src.screens.giveaway_screens.screens import Screen
import qtawesome as qta
from style import styling


class MainWindow(QMainWindow):
    SIDEBAR_OPEN_WIDTH = 150
    SIDEBAR_CLOSED_WIDTH = 62

    def __init__(self):
        super().__init__()
        self.setWindowTitle("buddy")
        self.setFixedSize(580, 640)

        self._is_sidebar_open = True
        self._menu_buttons = []
        self._menu_section_labels = []
        self._page_index = {}

        self._build_ui()
        self.setStyleSheet(styling.body)

    def _build_ui(self) -> None:
        root = QWidget()
        self.setCentralWidget(root)

        shell = QHBoxLayout(root)
        shell.setContentsMargins(0, 0, 0, 0)
        shell.setSpacing(0)

        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setMinimumWidth(0)
        self.sidebar.setMaximumWidth(self.SIDEBAR_OPEN_WIDTH)

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 12, 10, 12)
        sidebar_layout.setSpacing(8)

        self.menu_toggle_btn = QPushButton()
        self.menu_toggle_btn.setIcon(qta.icon("fa5s.bars", color="white"))
        self.menu_toggle_btn.setToolTip("toggle menubar")
        self.menu_toggle_btn.setObjectName("menuToggle")
        self.menu_toggle_btn.clicked.connect(self.toggle_sidebar)
        sidebar_layout.addWidget(self.menu_toggle_btn)

        nav_items = [
            ("all", " Free Games", "fa5s.tags", styling.all_free_games_section_btn, "black", "All Free to Play Games", Screen.all_games),
            ("ai", " Chatbot ", "fa5s.robot", styling.ai_chat_section_btn, "black", "AI powered chat", Screen.ai_chat),
            ("epic_games", " Epic Games", "./icons/epic_games.png", styling.epic_games_section_btn, "black", "Epic Games Giveaways", Screen.epic_games),
            ("steam", " Steam", "fa6b.steam", styling.steam_section_btn, "white", "Steam Giveaways", Screen.steam),
            ("ubisoft", " Ubisoft", "./icons/ubisoft.png", styling.ubisoft_section_btn, "black", "Ubisoft Giveaways", Screen.ubisoft),
            ("battlenet", " Battlenet", "./icons/battlenet.png", styling.battlenet_section_btn, "blue", "Battlenet Giveaways", Screen.battlenet),
            ("xbox", " Xbox", "fa6b.xbox", styling.xbox_section_btn, "white", "Xbox Gaming Stuff Giveaways", Screen.xbox),
            ("playstation", " PlayStation", "fa5b.playstation", styling.playstation_section_btn, "black", "PlayStation Gaming Stuff Giveaways", Screen.playstation),
            ("switch", " Switch", "./icons/switch.png", styling.switch_section_btn, "white", "Switch Gaming Stuff Giveaways", Screen.switch),
            ("android", " Android", "fa6b.android", styling.android_section_btn, "green", "Android Games Giveaways", Screen.android),
            ("ios", " iOS", "fa6b.apple", styling.ios_section_btn, "white", "iOS Games Giveaways", Screen.ios),
        ]

        self.stack = QStackedWidget()
        self.stack.setObjectName("contentArea")

        for key, label, icon, style, color, tooltip, page_class in nav_items:
            btn = QPushButton(label)
            if not icon.startswith("f"):
                btn.setIcon(QIcon(icon))
                btn.setIconSize(QSize(20, 20))
            else:
                btn.setIcon(qta.icon(icon, color=color))
            btn.setFont(QFont("monospace", 14))
            btn.setObjectName(key)
            btn.setToolTip(tooltip)
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            btn.setCheckable(True)
            btn.setProperty("full_label", label)
            btn.setProperty("short_label", label[0])
            btn.setStyleSheet(style)
            btn.clicked.connect(lambda checked=False, name=key: self.show_page(name))
            sidebar_layout.addWidget(btn)
            self._menu_buttons.append((key, btn))

            page = page_class()
            page_idx = self.stack.addWidget(page)
            self._page_index[key] = page_idx

            if key == "ai":
                section_label = QLabel("Giveaways")
                section_label.setProperty("full_label", "Giveaways")
                section_label.setProperty("short_label", "-----")
                section_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                section_label.setStyleSheet(
                    "color: #8a8f99; font-size: 11px; font-weight: 600; letter-spacing: 1px; margin-top: 8px;"
                )
                sidebar_layout.addWidget(section_label)
                self._menu_section_labels.append(section_label)

        sidebar_layout.addStretch(1)

        content_shell = QWidget()
        content_layout = QVBoxLayout(content_shell)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(self.stack)

        shell.addWidget(self.sidebar)
        shell.addWidget(content_shell, 1)

        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"maximumWidth", self)
        self.sidebar_min_animation = QPropertyAnimation(self.sidebar, b"minimumWidth", self)
        self.sidebar_animation_group = QParallelAnimationGroup(self)
        self.sidebar_animation_group.addAnimation(self.sidebar_animation)
        self.sidebar_animation_group.addAnimation(self.sidebar_min_animation)
        self.sidebar_animation.finished.connect(self._sync_sidebar_button_labels)

        for animation in (self.sidebar_animation, self.sidebar_min_animation):
            animation.setDuration(220)
            animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.show_page("search")



    def toggle_sidebar(self) -> None:
        target_width = (
            self.SIDEBAR_CLOSED_WIDTH if self._is_sidebar_open else self.SIDEBAR_OPEN_WIDTH
        )
        self._is_sidebar_open = not self._is_sidebar_open

        if self._is_sidebar_open:
            self._sync_sidebar_button_labels()

        current_width = self.sidebar.width()
        self.sidebar_animation_group.stop()

        self.sidebar_animation.setStartValue(current_width)
        self.sidebar_animation.setEndValue(target_width)
        self.sidebar_min_animation.setStartValue(current_width)
        self.sidebar_min_animation.setEndValue(target_width)
        self.sidebar_animation_group.start()

    def _sync_sidebar_button_labels(self) -> None:

        if self._is_sidebar_open:
            self.menu_toggle_btn.setText("Menu")
        else:
            self.menu_toggle_btn.setText("M")

        for _, btn in self._menu_buttons:
            if self._is_sidebar_open:
                btn.setText(btn.property("full_label"))
            else:
                btn.setText(btn.property("short_label"))

        for label in self._menu_section_labels:
            if self._is_sidebar_open:
                label.setText(label.property("full_label"))
            else:
                label.setText(label.property("short_label"))

    def show_page(self, page_name: str) -> None:
        idx = self._page_index.get(page_name)
        if idx is None:
            return

        self.stack.setCurrentIndex(idx)
        for key, btn in self._menu_buttons:
            btn.setChecked(key == page_name)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
