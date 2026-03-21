from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel


class BaseScreen(QWidget):
    def __init__(self, title: str, subtitle: str):
        super().__init__()

        root = QVBoxLayout(self)
        root.setContentsMargins(40, 40, 40, 40)
        root.setSpacing(12)
        root.setAlignment(Qt.AlignmentFlag.AlignTop)

        heading = QLabel(title)
        heading.setObjectName("screenTitle")

        description = QLabel(subtitle)
        description.setWordWrap(True)
        description.setObjectName("screenSubtitle")

        root.addWidget(heading)
        root.addWidget(description)
