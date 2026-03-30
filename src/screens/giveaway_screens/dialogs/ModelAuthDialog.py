from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel, QComboBox, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon, QCursor
from ....ai_integration import providers
from ....app_icon import app_window_icon
import qtawesome as qta
import yaml
import os


class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.provider = None

        with open("./config.yaml", "r") as file:
            self.models_config = yaml.safe_load(file)

        self.setWindowTitle("Selection Model Provider")
        self.setWindowIcon(app_window_icon())
        self.setFixedSize(420, 330)
        self.setModal(True)

        self.setStyleSheet("""
            QDialog {
                background: #0d1117;
                color: #e6edf3;
                border: 1px solid #30363d;
                border-radius: 14px;
            }

            QLabel#title {
                color: #f0f6fc;
                font-size: 16px;
                font-weight: 700;
            }

            QComboBox {
                background: #161b22;
                border: 1px solid #30363d;
                border-radius: 10px;
                color: #f0f6fc;
                padding: 8px 10px;
                selection-background-color: #2f81f7;
            }
            
            QLineEdit {
                background: #161b22;
                border: 1px solid #30363d;
                border-radius: 10px;
                color: #f0f6fc;
                padding: 8px 10px;
                selection-background-color: #2f81f7;
            }

            QLineEdit:focus {
                border: 1px solid #2f81f7;
            }

            QLineEdit::placeholder {
                color: #6e7681;
            }

            QPushButton {
                background: #238636;
                color: #ffffff;
                border: none;
                border-radius: 10px;
                padding: 10px 14px;
                font-weight: 600;
            }

            QPushButton:hover {
                background: #2ea043;
            }

            QPushButton:pressed {
                background: #1f7a31;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 22, 24, 22)
        layout.setSpacing(12)

        title = QLabel("Selected Model Provider and add your API KEY!")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 11))
        self.title = title

        # Providers Combox
        self.providers = QComboBox()
        self.providers.setPlaceholderText("Select Provider")
        self.items = {
            "OpenAI": providers.OPENAI_API_KEY,
            "Google": providers.GOOGLE_GEN_AI_API_KEY,
            "Anthropic": providers.ANTHROPIC_API_KEY,
            "Ollama Cloud": providers.OLLAMA_CLOUD_API_KEY
        }
        self.providers.addItems(self.items.keys())
        self.providers.setMinimumHeight(38)
        self.providers.currentTextChanged.connect(self.get_provider)

        # API KEY Input
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter your API KEY")
        self.api_key_input.setMinimumHeight(38)

        self.save_btn = QPushButton(" Save")
        self.save_btn.setFixedHeight(40)
        self.save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn.setIcon(QIcon(qta.icon("fa5s.save", color="#ffffff")))
        self.save_btn.setToolTip("Save data to MongoDB")
        self.save_btn.clicked.connect(self.save_model_provider_api_key)

        self.loader = QLabel("Adding API KEY...")
        self.loader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loader.setFont(QFont("Segoe UI", 10))
        self.loader.hide()

        layout.addWidget(title)
        layout.addSpacing(4)
        layout.addWidget(self.providers)
        layout.addWidget(self.api_key_input)
        layout.addSpacing(6)
        layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loader)

        self.setLayout(layout)

    def get_provider(self, model_provider):
        self.provider = model_provider

    def save_model_provider_api_key(self):
        apikey = self.api_key_input.text()
        if not self.provider:
            self.warnMessageBox("Oops!", "Please select a model provider!")
            return

        if not apikey:
            self.warnMessageBox("Oops!", "Please proivde a valid API KEY!")
            return

        models_config_path = "./config.yaml"

        if not os.path.exists(models_config_path):
            self.errorMessageBox(
                "Oops!", "./config.yaml file is not found! Please recheck it create new one.")
            return

        # set new api key
        with open(models_config_path, "w") as file:
            if str(self.provider).lower().startswith("openai"):
                self.models_config["openai"]["api_key"] = apikey
                yaml.safe_dump(self.models_config, file)
                self.infoMessageBox(
                    "Great!", f"API KEY se added for {self.provider}")
                return

            if str(self.provider).lower().startswith("google"):
                self.models_config["google_genai"]["api_key"] = apikey
                yaml.safe_dump(self.models_config, file)
                self.infoMessageBox(
                    "Great!", f"API KEY se added for {self.provider}")
                return

            if str(self.provider).lower().startswith("anthropic"):
                self.models_config["anthropic"]["api_key"] = apikey
                yaml.safe_dump(self.models_config, file)
                self.infoMessageBox(
                    "Great!", f"API KEY se added for {self.provider}")
                return

            if str(self.provider).lower().startswith("ollama"):
                self.models_config["ollama_cloud"]["api_key"] = apikey
                yaml.safe_dump(self.models_config, file)
                self.infoMessageBox(
                    "Great!", f"API KEY se added for {self.provider}")
                return

    def warnMessageBox(self, title: str, message: str):
        warn = QMessageBox()
        warn.setWindowIcon(app_window_icon())
        warn.setWindowTitle(title)
        warn.setText(message)
        warn.setIcon(QMessageBox.Icon.Warning)
        warn.setStandardButtons(QMessageBox.StandardButton.Ok)
        warn.exec()

    def errorMessageBox(self, title: str, message: str):
        critical = QMessageBox()
        critical.setWindowIcon(app_window_icon())
        critical.setWindowTitle(title)
        critical.setText(message)
        critical.setIcon(QMessageBox.Icon.Critical)
        critical.setStandardButtons(QMessageBox.StandardButton.Close)
        critical.exec()

    def infoMessageBox(self, title: str, message: str):
        info = QMessageBox()
        info.setWindowIcon(app_window_icon())
        info.setWindowTitle(title)
        info.setText(message)
        info.setIcon(QMessageBox.Icon.Information)
        info.setStandardButtons(QMessageBox.StandardButton.Ok)
        info.exec()
