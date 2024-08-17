from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal


class ClickableLabel(QLabel):
    clicked = pyqtSignal(int, int)  # Signal to emit the position of the clicked piece

    def __init__(self, row, col, parent=None):
        super().__init__(parent)
        self.row = row
        self.col = col

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.row, self.col)  # Emit the row and column when clicked