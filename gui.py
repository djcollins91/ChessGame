import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt
from helper import board_width

class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        GAME_TITLE = "Chess"
        GAME_WIDTH = 500
        GAME_HEIGHT = 500
         # Set up the main window
        self.setWindowTitle(GAME_TITLE)
        self.setFixedSize(GAME_WIDTH, GAME_HEIGHT)  # Fixed window size to prevent stretching

        # Set up the central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)
        central_widget.setLayout(grid_layout)

        # Define the size of each square
        SQUARE_SIZE = 50

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
            (0,6): 'WN',

            #black pawns
            (6,0): 'BP',
            (6,1): 'BP',
            (6,2): 'BP',
            (6,3): 'BP',
            (6,4): 'BP',
            (6,5): 'BP',
            (6,6): 'BP',
            (6,7): 'BP',
            
            #black rooks
            (7, 0): 'BR',
            (7, 7): 'BR',

            #black kings
            (7,4): 'BK',

            #black queens
            (7,3): 'BQ',

            #white bishops
            (7,2): 'BB',
            (7,5): 'BB',

            #black knights
            (7,1): 'BN',
            (7,6): 'BN',
        }
        white = QColor(255, 255, 255)
        blue = QColor(173, 216, 230)
        # Create the 8x8 grid of squares
        for row in board_width:
            for col in board_width:
                # Create a new widget for each square
                square = QWidget()
                color = white if (row + col) % 2 == 0 else blue
                square.setStyleSheet(f"background-color: {color.name()};")
                square.setFixedSize(SQUARE_SIZE, SQUARE_SIZE)
                
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
            'WR': 'piece_images/white/WR.png',
            'WP': 'piece_images/white/WP.png',
            'WK': 'piece_images/white/WK.png',
            'WQ': 'piece_images/white/WQ.png',
            'WB': 'piece_images/white/WB.png',
            'WN': 'piece_images/white/WN.png',
            'BP': 'piece_images/black/BP.png',
            'BR': 'piece_images/black/BR.png',
            'BK': 'piece_images/black/BK.png',
            'BQ': 'piece_images/black/BQ.png',
            'BB': 'piece_images/black/BB.png',
            'BN': 'piece_images/black/BN.png'

        }
        image_file = piece_images.get(piece, 'default.png')
        pixmap = QPixmap(image_file)
    
        # Resize the pixmap to fit the square (SQUARE_SIZE x SQUARE_SIZE)
        SQUARE_SIZE = 50  # You might want to make this a class attribute if it's used elsewhere
        pixmap = pixmap.scaled(SQUARE_SIZE, SQUARE_SIZE, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
        return pixmap

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = GameBoard()
    sys.exit(app.exec_())
