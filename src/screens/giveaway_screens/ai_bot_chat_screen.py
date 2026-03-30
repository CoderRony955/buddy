from PyQt6.QtCore import Qt, QTimer, QPoint, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QAction, QIcon, QTextOption
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QTextBrowser,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QToolBar,
    QMessageBox,
    QComboBox
)

from .base_screen import BaseScreen
import qtawesome as qta
import webbrowser
import style
import os

# dialog
from .dialogs import ModelAuthDialog

# model chat integration
from ...ai_integration import model
from ...app_icon import app_window_icon

# model chat worker (thread)
from ..threads import model_worker


class AutoResizeTextEdit(QTextEdit):
    send_requested = pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
                super().keyPressEvent(event)
                return
            self.send_requested.emit()
            event.accept()
            return
        super().keyPressEvent(event)


class UpwardComboBox(QComboBox):
    def showPopup(self):
        super().showPopup()

        popup = self.view().window()  # dropdown window
        combo_pos = self.mapToGlobal(QPoint(0, 0))

        # Move popup above the combo box
        popup.move(
            combo_pos.x(),
            combo_pos.y() - popup.height()
        )


class AIChatbotScreen(BaseScreen):
    def __init__(self):
        super().__init__(
            "Chat with AI (powered by AI)",
            "Chat with AI Bot to ask for games recommendation and much more.",
        )

        self.provider = None
        self.chat_client = model.Chat()
        self.chat_worker = None
        self.typing_timer = QTimer(self)
        self.typing_timer.setInterval(350)
        self.typing_timer.timeout.connect(self._update_typing_indicator)
        self.typing_bubble = None
        self.typing_dot_count = 0
        self.bot_bubbles = []
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

        self.message_input = AutoResizeTextEdit()
        self.message_input.setPlaceholderText("Type your message...")
        self.message_input.setFont(QFont("monospace", 10))
        self.message_input.setMinimumHeight(38)
        self.message_input.setMaximumHeight(140)
        self.message_input.setAcceptRichText(False)
        self.message_input.setWordWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
        self.message_input.textChanged.connect(self._adjust_input_height)
        self.message_input.send_requested.connect(self.send_message)
        self.message_input.setStyleSheet(
            """
            QTextEdit {
                background: #0d1020;
                color: #f5f7ff;
                border: 1px solid #2c3550;
                border-radius: 10px;
                padding: 6px 12px;
            }
            QTextEdit:focus {
                border: 1px solid #4f79ff;
            }
            """
        )

        # Providers Combox
        self.providers = UpwardComboBox()
        self.providers.setPlaceholderText("Select Provider")
        self.items = [
            "OpenAI",
            "Google",
            "Anthropic",
            "Ollama Cloud"
        ]
        self.providers.addItems(self.items)
        self.providers.setMinimumHeight(38)
        self.providers.currentTextChanged.connect(self.get_provider)
        self.providers.setStyleSheet("""
                            QComboBox {
                                    background: #161b22;
                                    border: 1px solid #30363d;
                                    border-radius: 10px;
                                    color: #f0f6fc;
                                    padding: 8px 10px;
                                    selection-background-color: #2f81f7;
                                }
                                     
            """)

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
        input_layout.addWidget(self.providers)
        input_layout.addWidget(self.send_btn)

        layout.addWidget(toolbar, 0)
        layout.addWidget(self.chat_scroll, 1)
        layout.addWidget(self.input_bar)

        self._append_message(
            "bot",
            "Hi! I am your game assistant. Ask me for free-to-play game suggestions.",
        )
        self._adjust_input_height()

    def send_message(self):
        text = self.message_input.toPlainText().strip()
        if not text:
            return

        self._append_message("user", text)
        self.message_input.clear()
        self._adjust_input_height()

        self.send_btn.setDisabled(True)
        self._start_typing_indicator()
        self.chat_worker = model_worker.ModelChatWorker(self.chat_client, self.provider, text)
        self.chat_worker.completed.connect(self._bot_reply)
        self.chat_worker.finished.connect(self.chat_worker.deleteLater)
        self.chat_worker.start()

    def _bot_reply(self, result):
        if isinstance(result, tuple) and len(result) >= 2 and result[0] is False:
            reply = f"Error: {result[1]}"
        elif isinstance(result, str):
            reply = result
        else:
            reply = "I could not parse the model response."

        self._stop_typing_indicator(reply)
        self.send_btn.setDisabled(False)
        self.message_input.setFocus()

    def _append_message(self, sender: str, text: str, markdown: bool = False):
        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)

        if sender == "user":
            bubble = QLabel(text)
            bubble.setWordWrap(True)
            bubble.setTextInteractionFlags(
                Qt.TextInteractionFlag.TextSelectableByMouse
            )
            bubble.setMaximumWidth(360)
            bubble.setSizePolicy(QSizePolicy.Policy.Maximum,
                                 QSizePolicy.Policy.Preferred)
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
            bubble = QTextBrowser()
            bubble.setOpenExternalLinks(True)
            bubble.setFrameShape(QFrame.Shape.NoFrame)
            bubble.setReadOnly(True)
            bubble.setUndoRedoEnabled(False)
            bubble.setVerticalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff
            )
            bubble.setHorizontalScrollBarPolicy(
                Qt.ScrollBarPolicy.ScrollBarAlwaysOff
            )
            bubble.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
            bubble.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)
            bubble.setSizePolicy(QSizePolicy.Policy.Maximum,
                                 QSizePolicy.Policy.Preferred)
            bubble.document().setDefaultStyleSheet(
                (
                    "p, li { white-space: pre-wrap; overflow-wrap: anywhere; }"
                    "pre, code { white-space: pre-wrap; word-wrap: break-word; overflow-wrap: anywhere; }"
                )
            )
            bubble.setStyleSheet(
                """
                QTextBrowser {
                    background: #1b2238;
                    color: #e8ecf9;
                    border-radius: 15px;
                    padding: 10px 12px;
                    border: none;
                }
                """
            )
            if markdown:
                bubble.setMarkdown(text)
            else:
                bubble.setPlainText(text)
            self._fit_bot_bubble_height(bubble)
            self.bot_bubbles.append(bubble)
            row.addWidget(bubble)
            row.addStretch(1)

        self.chat_layout.addLayout(row)
        QTimer.singleShot(0, self._scroll_to_bottom)
        return bubble

    def _scroll_to_bottom(self):
        scrollbar = self.chat_scroll.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def open_provider_auth_dialog(self):
        if not os.path.exists("./config.yaml"):
            # error message box
            title = "Oops"
            message = "./config.yaml file is not found! Please recheck it create new one."
            error = QMessageBox()
            error.setWindowIcon(app_window_icon())
            error.setWindowTitle(title)
            error.setText(message)
            error.setIcon(QMessageBox.Icon.Critical)
            error.setStandardButtons(QMessageBox.StandardButton.Close)
            error.exec()
            return

        db_dialog = ModelAuthDialog.AuthDialog()
        db_dialog.exec()
    
    def get_provider(self, model_provider):
        self.provider = model_provider

    def _adjust_input_height(self):
        doc_height = int(self.message_input.document().size().height())
        min_height = 38
        max_height = 140
        target = max(min_height, min(max_height, doc_height + 14))
        self.message_input.setFixedHeight(target)

    def _start_typing_indicator(self):
        self.typing_dot_count = 0
        self.typing_bubble = self._append_message("bot", "Typing")
        self.typing_timer.start()

    def _update_typing_indicator(self):
        if self.typing_bubble is None:
            self.typing_timer.stop()
            return
        self.typing_dot_count = (self.typing_dot_count + 1) % 4
        text = f"Typing{'.' * self.typing_dot_count}"
        self.typing_bubble.setPlainText(text)
        self._fit_bot_bubble_height(self.typing_bubble)
        self._scroll_to_bottom()

    def _stop_typing_indicator(self, final_reply: str):
        self.typing_timer.stop()
        if self.typing_bubble is not None:
            self.typing_bubble.setMarkdown(final_reply)
            self._fit_bot_bubble_height(self.typing_bubble)
            self.typing_bubble = None
            self.typing_dot_count = 0
            self._scroll_to_bottom()
            return

        self._append_message("bot", final_reply, markdown=True)

    def _fit_bot_bubble_height(self, bubble: QTextBrowser):
        available_width = self.chat_scroll.viewport().width()
        bubble_width = max(220, min(540, int(available_width * 0.72)))
        bubble.setFixedWidth(bubble_width)
        bubble.document().setTextWidth(bubble_width - 24)
        doc_height = int(bubble.document().size().height())
        bubble.setFixedHeight(doc_height + 24)
        bubble.updateGeometry()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        for bubble in self.bot_bubbles:
            self._fit_bot_bubble_height(bubble)
