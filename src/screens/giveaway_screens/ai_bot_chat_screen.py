from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QAction, QIcon
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QMessageBox
)

from .base_screen import BaseScreen
import qtawesome as qta
import webbrowser
import style
import os

# dialog
from .dialogs import ModelAuthDialog


class AIChatbotScreen(BaseScreen):
    def __init__(self):
        super().__init__(
            "Chat with AI (powered by AI)",
            "Chat with AI Bot to ask for games recommendation and much more.",
        )

        layout = self.layout()

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
        self.api_key_integration_btn = QAction()
        self.api_key_integration_btn.setToolTip("choose model provider")
        self.api_key_integration_btn.setIcon(
            QIcon(qta.icon("fa5s.key", style="white")))
        toolbar.addAction(self.api_key_integration_btn)
        self.api_key_integration_btn.triggered.connect(
            self.open_provider_auth_dialog)

        self.chat_scroll = QScrollArea()
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.chat_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.chat_scroll.setStyleSheet(
            "QScrollArea { background: transparent; border: none; }"
        )

        self.chat_body = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_body)
        self.chat_layout.setContentsMargins(0, 10, 0, 10)
        self.chat_layout.setSpacing(10)
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_scroll.setWidget(self.chat_body)

        self.input_bar = QFrame()
        self.input_bar.setStyleSheet(
            """
            QFrame {
                background: rgba(17, 20, 34, 0.85);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 15px;
            }
            """
        )

        input_layout = QHBoxLayout(self.input_bar)
        input_layout.setContentsMargins(8, 8, 8, 8)
        input_layout.setSpacing(8)

        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message...")
        self.message_input.setFont(QFont("monospace", 10))
        self.message_input.setMinimumHeight(38)
        self.message_input.setStyleSheet(
            """
            QLineEdit {
                background: #0d1020;
                color: #f5f7ff;
                border: 1px solid #2c3550;
                border-radius: 10px;
                padding: 0 12px;
            }
            QLineEdit:focus {
                border: 1px solid #4f79ff;
            }
            """
        )
        self.message_input.returnPressed.connect(self.send_message)

        self.send_btn = QPushButton()
        self.send_btn.setIcon(
            QIcon(qta.icon("fa5s.paper-plane", style="white")))
        self.send_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.send_btn.setMinimumHeight(38)
        self.send_btn.setFixedWidth(56)
        self.send_btn.setStyleSheet(
            """
            QPushButton {
                background: #1f8f68;
                color: white;
                border: none;
                border-radius: 15px;
                font-weight: 700;
            }
            QPushButton:hover {
                background: #28a377;
            }
            QPushButton:disabled {
                background: #586069;
                color: #d3d7dc;
            }
            """
        )
        self.send_btn.clicked.connect(self.send_message)

        input_layout.addWidget(self.message_input, 1)
        input_layout.addWidget(self.send_btn)

        layout.addWidget(toolbar, 0)
        layout.addWidget(self.chat_scroll, 1)
        layout.addWidget(self.input_bar)

        self._append_message(
            "bot",
            "Hi! I am your game assistant. Ask me for free-to-play game suggestions.",
        )

    def send_message(self):
        text = self.message_input.text().strip()
        if not text:
            return

        self._append_message("user", text)
        self.message_input.clear()

        self.send_btn.setDisabled(True)
        QTimer.singleShot(250, lambda: self._bot_reply(text))

    def _bot_reply(self, user_message: str):
        reply = (
            "I received: "
            f"'{user_message}'.\n"
            "AI backend is not connected yet, but the chat UI is ready."
        )
        self._append_message("bot", reply)
        self.send_btn.setDisabled(False)
        self.message_input.setFocus()

    def _append_message(self, sender: str, text: str):
        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)

        bubble = QLabel(text)
        bubble.setWordWrap(True)
        bubble.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        bubble.setMaximumWidth(360)
        bubble.setSizePolicy(QSizePolicy.Policy.Maximum,
                             QSizePolicy.Policy.Preferred)

        if sender == "user":
            row.addStretch(1)
            bubble.setStyleSheet(
                """
                QLabel {
                    background: #0b5a42;
                    color: #f4fffb;
                    border-radius: 15px;
                    padding: 10px 12px;
                }
                """
            )
            row.addWidget(bubble)
        else:
            bubble.setStyleSheet(
                """
                QLabel {
                    background: #1b2238;
                    color: #e8ecf9;
                    border-radius: 15px;
                    padding: 10px 12px;
                }
                """
            )
            row.addWidget(bubble)
            row.addStretch(1)

        self.chat_layout.addLayout(row)
        QTimer.singleShot(0, self._scroll_to_bottom)

    def _scroll_to_bottom(self):
        scrollbar = self.chat_scroll.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def open_provider_auth_dialog(self):
        if not os.path.exists("./config.yaml"):
            # error message box
            title = "Oops"
            message = "./config.yaml file is not found! Please recheck it create new one."
            error = QMessageBox()
            error.setWindowTitle(title)
            error.setText(message)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setStandardButtons(QMessageBox.StandardButton.Close)
            error.exec()
            return

        db_dialog = ModelAuthDialog.AuthDialog()
        db_dialog.exec()
