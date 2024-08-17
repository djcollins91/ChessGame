from PyQt5.QtWidgets import  QMainWindow, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt

# Assuming all the piece classes and Board class are properly imported here
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
from board import Board
from clickable_label import ClickableLabel


class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = Board()  # Initialize your Board here
        self.init_ui()

    def init_ui(self):
        GAME_TITLE = "Chess"
        GAME_WIDTH = 500
        GAME_HEIGHT = 500

        self.setWindowTitle(GAME_TITLE)
        self.setFixedSize(GAME_WIDTH, GAME_HEIGHT)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.grid_layout = QGridLayout(central_widget)
        central_widget.setLayout(self.grid_layout)

        SQUARE_SIZE = 50

        board_setup = {
            # White pieces
            (1, 0): White_Pawn("White Pawn"),
            (1, 1): White_Pawn("White Pawn"),
            (1, 2): White_Pawn("White Pawn"),
            (1, 3): White_Pawn("White Pawn"),
            (1, 4): White_Pawn("White Pawn"),
            (1, 5): White_Pawn("White Pawn"),
            (1, 6): White_Pawn("White Pawn"),
            (1, 7): White_Pawn("White Pawn"),
            (0, 0): White_Rook("White Rook"),
            (0, 7): White_Rook("White Rook"),
            (0, 4): White_King("White King"),
            (0, 3): White_Queen("White Queen"),
            (0, 2): White_Bishop("White Bishop"),
            (0, 5): White_Bishop("White Bishop"),
            (0, 1): White_Knight("White Knight"),
            (0, 6): White_Knight("White Knight"),
            # Black pieces
            (6, 0): Black_Pawn("Black Pawn"),
            (6, 1): Black_Pawn("Black Pawn"),
            (6, 2): Black_Pawn("Black Pawn"),
            (6, 3): Black_Pawn("Black Pawn"),
            (6, 4): Black_Pawn("Black Pawn"),
            (6, 5): Black_Pawn("Black Pawn"),
            (6, 6): Black_Pawn("Black Pawn"),
            (6, 7): Black_Pawn("Black Pawn"),
            (7, 0): Black_Rook("Black Rook"),
            (7, 7): Black_Rook("Black Rook"),
            (7, 4): Black_King("Black King"),
            (7, 3): Black_Queen("Black Queen"),
            (7, 2): Black_Bishop("Black Bishop"),
            (7, 5): Black_Bishop("Black Bishop"),
            (7, 1): Black_Knight("Black Knight"),
            (7, 6): Black_Knight("Black Knight"),
        }

        for pos, piece in board_setup.items():
            self.board.place_piece(piece, pos[1], pos[0])  # Place piece on the internal board

        white = QColor(255, 255, 255)
        blue = QColor(173, 216, 230)

        for row in range(Board.getLENGTH()):
            for col in range(Board.getWIDTH()):
                square = QWidget()
                color = white if (row + col) % 2 == 0 else blue
                square.setStyleSheet(f"background-color: {color.name()};")
                square.setFixedSize(SQUARE_SIZE, SQUARE_SIZE)
                
                self.grid_layout.addWidget(square, row, col)

                piece = self.board.grid[row][col]
                if piece:
                    piece_label = ClickableLabel(row, col)
                    piece_label.setPixmap(self.get_piece_pixmap(piece))
                    piece_label.setAlignment(Qt.AlignCenter)
                    piece_label.clicked.connect(self.on_piece_clicked)
                    self.grid_layout.addWidget(piece_label, row, col)

        self.show()

    def get_piece_pixmap(self, piece):
        piece_images = {
            'White_Rook': 'piece_images/white/WR.png',
            'White_Pawn': 'piece_images/white/WP.png',
            'White_King': 'piece_images/white/WK.png',
            'White_Queen': 'piece_images/white/WQ.png',
            'White_Bishop': 'piece_images/white/WB.png',
            'White_Knight': 'piece_images/white/WN.png',
            'Black_Pawn': 'piece_images/black/BP.png',
            'Black_Rook': 'piece_images/black/BR.png',
            'Black_King': 'piece_images/black/BK.png',
            'Black_Queen': 'piece_images/black/BQ.png',
            'Black_Bishop': 'piece_images/black/BB.png',
            'Black_Knight': 'piece_images/black/BN.png'
        }

        piece_name = type(piece).__name__
        image_file = piece_images.get(piece_name, 'default.png')
        pixmap = QPixmap(image_file)
        SQUARE_SIZE = 50
        pixmap = pixmap.scaled(SQUARE_SIZE, SQUARE_SIZE, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        return pixmap

    def on_piece_clicked(self, row, col):
        piece = self.board.grid[row][col]
        if piece:
            print(f"Clicked on {piece} at position ({row}, {col})")
            # Add your move logic here

