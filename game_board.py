from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QMessageBox, QLabel
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
from Pieces.empty.empty import Empty_Spot
from board import Board
from clickable_label import ClickableLabel
from computer_player import Computer_Player
from human_player import Human_Player
SQUARE_SIZE = 50
class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = Board()  # Initialize your Board here
        self.selected_piece = None
        self.selected_position = None
        self.labels = {}  # To store references to labels for updating squares
        self.init_ui()
    turnVar = True
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
    
        

        board_setup = {
            #Empty Spaces
            (2, 0): Empty_Spot("Empty Spot"),
            (2, 1): Empty_Spot("Empty Spot"),
            (2, 2): Empty_Spot("Empty Spot"),
            (2, 3): Empty_Spot("Empty Spot"),
            (2, 4): Empty_Spot("Empty Spot"),
            (2, 5): Empty_Spot("Empty Spot"),
            (2, 6): Empty_Spot("Empty Spot"),
            (2, 7): Empty_Spot("Empty Spot"),
            
            (3, 0): Empty_Spot("Empty Spot"),
            (3, 1): Empty_Spot("Empty Spot"),
            (3, 2): Empty_Spot("Empty Spot"),
            (3, 3): Empty_Spot("Empty Spot"),
            (3, 4): Empty_Spot("Empty Spot"),
            (3, 5): Empty_Spot("Empty Spot"),
            (3, 6): Empty_Spot("Empty Spot"),
            (3, 7): Empty_Spot("Empty Spot"),

            (4, 0): Empty_Spot("Empty Spot"),
            (4, 1): Empty_Spot("Empty Spot"),
            (4, 2): Empty_Spot("Empty Spot"),
            (4, 3): Empty_Spot("Empty Spot"),
            (4, 4): Empty_Spot("Empty Spot"),
            (4, 5): Empty_Spot("Empty Spot"),
            (4, 6): Empty_Spot("Empty Spot"),
            (4, 7): Empty_Spot("Empty Spot"),

            (5, 0): Empty_Spot("Empty Spot"),
            (5, 1): Empty_Spot("Empty Spot"),
            (5, 2): Empty_Spot("Empty Spot"),
            (5, 3): Empty_Spot("Empty Spot"),
            (5, 4): Empty_Spot("Empty Spot"),
            (5, 5): Empty_Spot("Empty Spot"),
            (5, 6): Empty_Spot("Empty Spot"),
            (5, 7): Empty_Spot("Empty Spot"),
            # White pieces
            (1, 0): Black_Pawn("Black Pawn"),
            (1, 1): Black_Pawn("Black Pawn"),
            (1, 2): Black_Pawn("Black Pawn"),
            (1, 3): Black_Pawn("Black Pawn"),
            (1, 4): Black_Pawn("Black Pawn"),
            (1, 5): Black_Pawn("Black Pawn"),
            (1, 6): Black_Pawn("Black Pawn"),
            (1, 7): Black_Pawn("Black Pawn"),
            (0, 0): White_Rook("White Rook"),
            (0, 7): White_Rook("White Rook"),
            (0, 4): White_King("White King"),
            (0, 3): White_Queen("White Queen"),
            (0, 2): White_Bishop("White Bishop"),
            (0, 5): White_Bishop("White Bishop"),
            (0, 1): White_Knight("White Knight"),
            (0, 6): White_Knight("White Knight"),
            # Black pieces
            (6, 0): White_Pawn("White Pawn"),
            (6, 1): White_Pawn("White Pawn"),
            (6, 2): White_Pawn("White Pawn"),
            (6, 3): White_Pawn("White Pawn"),
            (6, 4): White_Pawn("White Pawn"),
            (6, 5): White_Pawn("White Pawn"),
            (6, 6): White_Pawn("White Pawn"),
            (6, 7): White_Pawn("White Pawn"),
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
                    self.labels[(row, col)] = piece_label  # Store label reference

        self.show()
    def remove_piece(self, position):
        if position in self.board_setup:
            del self.board_setup[position]
            self.refresh_ui()
    def set_piece(self, position, piece):
        self.board_setup[position] = piece
        self.refresh_ui()
    def refresh_ui(self):
        # Clear the current layout
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # Re-add all pieces based on the updated board_setup
        for (row, col), piece in self.board_setup.items():
            label = QLabel(piece.name)  # Assuming each piece has a `name` attribute
            label.setFixedSize(SQUARE_SIZE, SQUARE_SIZE)
            label.setAlignment(Qt.AlignCenter)
            self.grid_layout.addWidget(label, row, col)


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
        player1 = Human_Player("Player1", self.board)
        player2 = Human_Player("Player2", self.board)
        current_turn = GameBoard.turnVar  # True for Black's turn, False for White's turn
        piece = self.board.grid[row][col]

        if self.selected_piece is None:
            # First click: Selecting a piece
            if (current_turn and piece and str(piece).startswith('B')) or \
            (not current_turn and piece and str(piece).startswith('W')):
                self.selected_piece = piece
                self.selected_position = (row, col)
                QMessageBox.information(self, "Move Piece",
                                        f"Selected {piece} at ({row}, {col}). Click on the destination.")
            else:
                QMessageBox.warning(self, "Invalid Selection", "Please select a valid piece for your turn.")
        else:
            # Second click: Moving the selected piece
            from_y, from_x = self.selected_position
            to_y, to_x = row, col

            valid_destination = (
                piece is None or  # Empty square
                (current_turn and str(piece).startswith('W')) or  # Black capturing White
                (not current_turn and str(piece).startswith('B')) or  # White capturing Black
                (str(piece).startswith('E') and ( player1.turn(self.board, from_x, from_y, to_x, to_y, piece))) # Empty spot
            )

            if valid_destination:
                # Perform the move
                self.board.place_piece(self.selected_piece, to_y, to_x)
                self.board.grid[from_y][from_x] = Empty_Spot("Empty Spot")  # Clear old spot

                # Update the UI
                self.update_square(from_y, from_x, None)
                self.update_square(to_y, to_x, self.selected_piece)

                # Reset the selection
                self.selected_piece = None
                self.selected_position = None

                # Switch the turn
                GameBoard.turnVar = not GameBoard.turnVar
            else:
                QMessageBox.warning(self, "Invalid Move", "Cannot move to that square.")



    def update_square(self, row, col, piece):
        label = self.labels.get((row, col))
        if label:
            if piece:
                label.setPixmap(self.get_piece_pixmap(piece))
            else:
                label.clear()  # Clears the label content for an empty square
                self.labels.pop((row, col), None)  # Remove the reference
        else:
            if piece:
                new_label = ClickableLabel(row, col)
                new_label.setPixmap(self.get_piece_pixmap(piece))
                new_label.setAlignment(Qt.AlignCenter)
                new_label.clicked.connect(self.on_piece_clicked)
                self.grid_layout.addWidget(new_label, row, col)
                self.labels[(row, col)] = new_label



