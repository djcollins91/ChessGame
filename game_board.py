from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


from pieces.empty.empty import Empty_Spot
from place_pieces import LOOP_SIZE


class GameBoard(QWidget):
    turnVar = False  # False = Black's turn, True = White's turn

    def __init__(self, board):
        super().__init__()
        self.setWindowTitle("Chess Game")
        self.board = board
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.buttons = [[None for _ in range(LOOP_SIZE)] for _ in range(LOOP_SIZE)]
        self.selected_pos = None
        self.init_board()

    def init_board(self):
        for row in range(LOOP_SIZE):
            for col in range(LOOP_SIZE):
                self.update_square(row, col, self.board.grid[row][col])

    def update_square(self, row, col, piece):
        # Remove old button if one exists
        if self.buttons[row][col] is not None:
            self.grid_layout.removeWidget(self.buttons[row][col])
            self.buttons[row][col].deleteLater()
        BUTTON_SIZE = 80
        button = QPushButton()
        button.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        color = "white" if (row + col) % 2 == 0 else "blue"
        button.setStyleSheet(f"background-color: {color};")

        if piece and str(piece) != Empty_Spot.get_str():
            folder = "white" if str(piece).startswith("W") else "black"
            icon_path = f"piece_images/{folder}/{piece.get_piece_str()}.png"
            button.setIcon(QIcon(icon_path))
            ICON_SIZE = 64
            button.setIconSize(QSize(ICON_SIZE, ICON_SIZE))

        button.clicked.connect(lambda _, r=row, c=col: self.handle_click(r, c))
        self.grid_layout.addWidget(button, row, col)
        self.buttons[row][col] = button

    def handle_click(self, row, col):
        clicked_piece = self.board.grid[row][col]
        print(f"Clicked on ({row},{col}) -> {clicked_piece}")

        if self.selected_pos is None:
            # Selecting a piece
            if clicked_piece and str(clicked_piece) != Empty_Spot.get_str():
                if (GameBoard.turnVar and str(clicked_piece).startswith("W")) or \
                (not GameBoard.turnVar and str(clicked_piece).startswith("B")):
                    self.selected_pos = (row, col)
                    QMessageBox.information(self, "Piece Selected", f"Selected piece at ({row},{col}). Now click a destination.")
                else:
                    QMessageBox.warning(self, "Wrong Turn", "It's not your turn.")
        else:
            from_row, from_col = self.selected_pos
            moving_piece = self.board.grid[from_row][from_col]
            target_piece = self.board.grid[row][col]

            valid = moving_piece.move(self.board, from_col, from_row, col, row)

            if valid:
                self.board.grid[row][col] = moving_piece
                self.board.grid[from_row][from_col] = Empty_Spot(Empty_Spot.get_str())

                self.update_square(from_row, from_col, self.board.grid[from_row][from_col])
                self.update_square(row, col, self.board.grid[row][col])

                QMessageBox.information(self, "Moved", f"Moved to ({row}, {col})")
                GameBoard.turnVar = not GameBoard.turnVar
            else:
                QMessageBox.warning(self, "Invalid Move", "That move is not allowed.")

            self.selected_pos = None

