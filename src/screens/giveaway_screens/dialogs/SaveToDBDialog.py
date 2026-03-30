from PyQt6.QtWidgets import QDialog, QPushButton, QLabel, QLineEdit, QVBoxLayout, QMessageBox
from PyQt6.QtGui import QFont, QIcon, QCursor
from PyQt6.QtCore import Qt
import qtawesome as qta
from ...threads import feed_data
from ....app_icon import app_window_icon
import json

class DBDialog(QDialog):
    def __init__(self, data_path: str):
        super().__init__()
        with open(data_path, "r") as file:
            self.data = json.load(file)
            
        self.setWindowTitle("Save to MongoDB")
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

            QLabel#description {
                color: #8b949e;
                font-size: 12px;
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
        
        title = QLabel("Want to save this data to your database?")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 11))
        self.title = title

        description = QLabel("buddy uses MongoDB to store fetched game data.")
        description.setObjectName("description")
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description.setWordWrap(True)
        description.setFont(QFont("Segoe UI", 9))
        self.description = description

        # DB URL
        self.cluster = QLineEdit()
        self.cluster.setPlaceholderText("Enter MongoDB connection URI")
        self.cluster.setMinimumHeight(38)

        # DB NAME
        self.dbname = QLineEdit()
        self.dbname.setPlaceholderText("Enter database name")
        self.dbname.setMinimumHeight(38)
        
        # COLLECTION NAME
        self.collection_name = QLineEdit()
        self.collection_name.setPlaceholderText("Enter collection name")
        self.collection_name.setMinimumHeight(38)

        self.save_btn = QPushButton(" Save to DB")
        self.save_btn.setFixedHeight(40)
        self.save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_btn.setIcon(QIcon(qta.icon("fa5s.save", color="#ffffff")))
        self.save_btn.setToolTip("Save data to MongoDB")
        self.save_btn.clicked.connect(self.feed_data_to_mongodb)

        self.loader = QLabel("Checking and feeding data...")
        self.loader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loader.setFont(QFont("Segoe UI", 10))
        self.loader.hide()

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addSpacing(4)
        layout.addWidget(self.cluster)
        layout.addWidget(self.dbname)
        layout.addWidget(self.collection_name)
        layout.addSpacing(6)
        layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loader)

        self.setLayout(layout)

        self.form_widgets = [
            self.title,
            self.description,
            self.cluster,
            self.dbname,
            self.collection_name,
            self.save_btn,
        ]
    
    def feed_data_to_mongodb(self):
        db_url = self.cluster.text()
        db_name = self.dbname.text()
        collection_name = self.collection_name.text()
        
        if not db_url:
            self.warnMessageBox("Oops!", "You forgot to input your MongoDB Cluster URL.")
            return
        
        elif not db_name:
            self.warnMessageBox("Oops!", "You forgot to input your MongoDB Database name.")
            return
        
        elif not collection_name:
            self.warnMessageBox("Oops!", "You forgot to input your MongoDB Database's Collection Name.")
            return

        self.set_loading(True)
            
        self.db = feed_data.Start(self.data, db_url, db_name, collection_name)
        self.db.data_feed_op.connect(self.data_feed_output)
        self.db.start()
    
    def data_feed_output(self, acknowledgment):
        self.set_loading(False)

        if isinstance(acknowledgment, tuple):
            # popup critical messagebox
            error = QMessageBox()
            error.setWindowIcon(app_window_icon())
            error.setWindowTitle("Oops!")
            error.setText(str(acknowledgment[0]))
            error.setIcon(QMessageBox.Icon.Critical)
            error.setStandardButtons(QMessageBox.StandardButton.Close)
            error.exec()
            return
        
        # otherwise popup informational messagebox for successful operation
        info = QMessageBox()
        info.setWindowIcon(app_window_icon())
        info.setWindowTitle("Done!")
        info.setText(str(acknowledgment))
        info.setIcon(QMessageBox.Icon.Information)
        info.setStandardButtons(QMessageBox.StandardButton.Ok)
        info.exec()
        
    def set_loading(self, is_loading: bool):
        for widget in self.form_widgets:
            widget.setVisible(not is_loading)
        self.loader.setVisible(is_loading)
    
    
    def warnMessageBox(self, title: str, message: str):
        warn = QMessageBox()
        warn.setWindowIcon(app_window_icon())
        warn.setWindowTitle(title)
        warn.setText(message)
        warn.setIcon(QMessageBox.Icon.Warning)
        warn.setStandardButtons(QMessageBox.StandardButton.Ok)
        warn.exec()
        
