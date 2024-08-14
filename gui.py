import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtGui import QColor
from helper import board_width

class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Chess")
        self.setGeometry(100, 100, 400, 400)

        # Set up the central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)
        central_widget.setLayout(grid_layout)

        # Define the size of each square
        square_size = 50
        white = QColor(255, 255, 255)
        blue = QColor(173, 216, 230)
        # Create the 8x8 grid of squares
        for row in board_width:
            for col in board_width:
                # Create a new widget for each square
                square = QWidget()
                color = white if (row + col) % 2 == 0 else blue
                square.setStyleSheet(f"background-color: {color.name()};")
                square.setFixedSize(square_size, square_size)
                
                # Add the square to the grid layout
                grid_layout.addWidget(square, row, col)

        self.show()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = GameBoard()
    sys.exit(app.exec_())
