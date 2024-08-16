import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt
from Pieces.bishops.black.black_bishop import Black_Bishop
from Pieces.bishops.white.white_bishop import White_Bishop
from Pieces.kings.black.black_king import Black_King
from Pieces.kings.white.white_king import White_King
from Pieces.knights.black.black_knight import Black_Knight
from Pieces.knights.white.white_knight import White_Knight
from Pieces.pawns.black.black_pawn import Black_Pawn
from Pieces.pawns.white.white_pawn import White_Pawn
from Pieces.queens.black.black_queen import Black_Queen
from Pieces.queens.white.white_queen import White_Queen
from Pieces.rooks.black.black_rook import Black_Rook
from Pieces.rooks.white.white_rook import White_Rook
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
            (1,0): White_Pawn.get_piece_str(),
            (1,1): White_Pawn.get_piece_str(),
            (1,2): White_Pawn.get_piece_str(),
            (1,3): White_Pawn.get_piece_str(),
            (1,4): White_Pawn.get_piece_str(),
            (1,5): White_Pawn.get_piece_str(),
            (1,6): White_Pawn.get_piece_str(),
            (1,7): White_Pawn.get_piece_str(),
        
            #white rooks
            (0, 0): White_Rook.get_piece_str(),
            (0, 7): White_Rook.get_piece_str(),

            #white kings
            (0,4): White_King.get_piece_str(),

            #white queens
            (0,3): White_Queen.get_piece_str(),

            #white bishops
            (0,2): White_Bishop.get_piece_str(),
            (0,5): White_Bishop.get_piece_str(),

            #white knights
            (0,1): White_Knight.get_piece_str(),
            (0,6): White_Knight.get_piece_str(),
            
            

            #black pawns
            (6,0): Black_Pawn.get_piece_str(),
            (6,1): Black_Pawn.get_piece_str(),
            (6,2): Black_Pawn.get_piece_str(),
            (6,3): Black_Pawn.get_piece_str(),
            (6,4): Black_Pawn.get_piece_str(),
            (6,5): Black_Pawn.get_piece_str(),
            (6,6): Black_Pawn.get_piece_str(),
            (6,7): Black_Pawn.get_piece_str(),
            
            #black rooks
            (7, 0): Black_Rook.get_piece_str(),
            (7, 7): Black_Rook.get_piece_str(),

            #black kings
            (7,4): Black_King.get_piece_str(),

            #black queens
            (7,3): Black_Queen.get_piece_str(),

            #white bishops
            (7,2): Black_Bishop.get_piece_str(),
            (7,5): Black_Bishop.get_piece_str(),

            #black knights
            (7,1): Black_Knight.get_piece_str(),
            (7,6): Black_Knight.get_piece_str(),
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
            White_Rook.get_piece_str(): 'piece_images/white/WR.png',
            White_Pawn.get_piece_str(): 'piece_images/white/WP.png',
            White_King.get_piece_str(): 'piece_images/white/WK.png',
            White_Queen.get_piece_str(): 'piece_images/white/WQ.png',
            White_Bishop.get_piece_str(): 'piece_images/white/WB.png',
            White_Knight.get_piece_str(): 'piece_images/white/WN.png',
            Black_Pawn.get_piece_str(): 'piece_images/black/BP.png',
            Black_Rook.get_piece_str(): 'piece_images/black/BR.png',
            Black_King.get_piece_str(): 'piece_images/black/BK.png',
            Black_Queen.get_piece_str(): 'piece_images/black/BQ.png',
            Black_Bishop.get_piece_str(): 'piece_images/black/BB.png',
            Black_Knight.get_piece_str(): 'piece_images/black/BN.png'

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
