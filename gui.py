import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt

class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("8x8 Game Board")
        self.setGeometry(100, 100, 400, 400)

        # Set up the central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)
        central_widget.setLayout(grid_layout)

        # Define the size of each square
        square_size = 50

        # Sample board setup: dictionary with piece positions
        board_setup = { 
            #white pawns   
            (1,0): 'WP',
            (1,1): 'WP',
            (1,2): 'WP',
            (1,3): 'WP',
            (1,4): 'WP',
            (1,5): 'WP',
            (1,6): 'WP',
            (1,7): 'WP',
            (1,8): 'WP',
            #white rooks
            (0, 0): 'WR',
            (0, 7): 'WR',
            #white kings
            (0,4): 'WK',
            #white queens
            (0,3): 'WQ',
            #white bishops
            (0,2): 'WB',
            (0,5): 'WB',
            #white knights
            (0,1): 'WN',
            (0,6): 'WN'


            
            # Add more pieces as needed
        }
        white = QColor(255, 255, 255)
        blue = QColor(173, 216, 230)
        # Create the 8x8 grid of squares
        for row in range(8):
            for col in range(8):
                # Create a new widget for each square
                square = QWidget()
                color = white if (row + col) % 2 == 0 else blue
                square.setStyleSheet(f"background-color: {color.name()};")
                square.setFixedSize(square_size, square_size)
                
                # Add the square to the grid layout
                grid_layout.addWidget(square, row, col)

                # Check if there's a piece in the current position
                piece = board_setup.get((row, col))
                if piece:
                    # Create a QLabel for the piece and set its pixmap
                    piece_label = QLabel()
                    piece_label.setPixmap(self.get_piece_pixmap(piece))
                    piece_label.setAlignment(Qt.AlignCenter)
                    grid_layout.addWidget(piece_label, row, col)

        self.show()

    def get_piece_pixmap(self, piece):
        # Map the piece type to an image file
        piece_images = {
            'WR': 'piece_images/WR.png',
            'WP': 'piece_images/WP.png',
            'WK': 'piece_images/WK.png',
            'WQ': 'piece_images/WQ.png',
            'WB': 'piece_images/WB.png',
            'WN': 'piece_images/WN.png'

            # Add more mappings for other pieces
        }
        image_file = piece_images.get(piece, 'default.png')
        pixmap = QPixmap(image_file)
    
        # Resize the pixmap to fit the square (square_size x square_size)
        square_size = 50  # You might want to make this a class attribute if it's used elsewhere
        pixmap = pixmap.scaled(square_size, square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
        return pixmap

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = GameBoard()
    sys.exit(app.exec_())
