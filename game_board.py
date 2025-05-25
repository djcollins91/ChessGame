from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


from pieces.kings.black.black_king import Black_King
from pieces.kings.white.white_king import White_King
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

    def is_king_in_check(self, color, board=None):
        # Returns True if the king of 'color' is in check on the given board (or self.board)
        if board is None:
            board = self.board
        king_str = 'WK' if color == 'white' else 'BK'
        king_pos = None
        for r in range(LOOP_SIZE):
            for c in range(LOOP_SIZE):
                if str(board.grid[r][c]) == king_str:
                    king_pos = (r, c)
                    break
            if king_pos:
                break
        if not king_pos:
            return False
        for r in range(LOOP_SIZE):
            for c in range(LOOP_SIZE):
                piece = board.grid[r][c]
                if (color == 'white' and str(piece).startswith('B')) or (color == 'black' and str(piece).startswith('W')):
                    if piece is not Empty_Spot and str(piece) != Empty_Spot.get_str():
                        take_piece_method = getattr(piece, 'take_piece', None)
                        if callable(take_piece_method):
                            if take_piece_method(board, c, r, king_pos[1], king_pos[0]):
                                return True
        return False

    def clone_board(self):
        # Returns a deep copy of the board object
        import copy
        return copy.deepcopy(self.board)

    def has_any_legal_moves(self, color):
        # Returns True if the player of 'color' has any legal move that gets out of check
        for r in range(LOOP_SIZE):
            for c in range(LOOP_SIZE):
                piece = self.board.grid[r][c]
                if (color == 'white' and str(piece).startswith('W')) or (color == 'black' and str(piece).startswith('B')):
                    # Try all possible destinations
                    for tr in range(LOOP_SIZE):
                        for tc in range(LOOP_SIZE):
                            if (r, c) == (tr, tc):
                                continue
                            # Simulate move
                            simulated_board = self.clone_board()
                            moving_piece = simulated_board.grid[r][c]
                            target_piece = simulated_board.grid[tr][tc]
                            # Only try if move is valid
                            move_method = getattr(moving_piece, 'move', None)
                            if callable(move_method) and move_method(simulated_board, c, r, tc, tr):
                                # Make the move
                                simulated_board.grid[tr][tc] = moving_piece
                                simulated_board.grid[r][c] = Empty_Spot(Empty_Spot.get_str())
                                # If king is not in check after this move, it's a legal move
                                if not self.is_king_in_check(color, simulated_board):
                                    return True
        return False

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

            # Determine current player color
            current_color = 'white' if GameBoard.turnVar else 'black'
            in_check = self.is_king_in_check(current_color)

            valid = moving_piece.move(self.board, from_col, from_row, col, row)

            if valid:
                # Simulate the move to check if it puts or leaves your own king in check
                simulated_board = self.clone_board()
                simulated_board.grid[row][col] = simulated_board.grid[from_row][from_col]
                simulated_board.grid[from_row][from_col] = Empty_Spot(Empty_Spot.get_str())
                still_in_check = self.is_king_in_check(current_color, simulated_board)

                if still_in_check:
                    QMessageBox.critical(self, "Illegal Move", "You cannot make a move that puts or leaves your own king in check!")
                    self.selected_pos = None
                    return

                self.board.grid[row][col] = moving_piece
                self.board.grid[from_row][from_col] = Empty_Spot(Empty_Spot.get_str())

                self.update_square(from_row, from_col, self.board.grid[from_row][from_col])
                self.update_square(row, col, self.board.grid[row][col])

                # --- Check detection: is any king in check after the move? ---
                for check_color, king_str in [("white", White_King.get_piece_str()), ("black", Black_King.get_piece_str())]:
                    king_pos = None
                    for r in range(LOOP_SIZE):
                        for c in range(LOOP_SIZE):
                            if str(self.board.grid[r][c]) == king_str:
                                king_pos = (r, c)
                                break
                        if king_pos:
                            break
                    king_in_check = False
                    if king_pos:
                        # Scan all opponent's pieces to see if any can take the king
                        for r in range(LOOP_SIZE):
                            for c in range(LOOP_SIZE):
                                piece = self.board.grid[r][c]
                                if (check_color == "white" and str(piece).startswith("B")) or (check_color == "black" and str(piece).startswith("W")):
                                    if piece is not Empty_Spot and str(piece) != Empty_Spot.get_str():
                                        take_piece_method = getattr(piece, 'take_piece', None)
                                        if callable(take_piece_method):
                                            if take_piece_method(self.board, c, r, king_pos[1], king_pos[0]):
                                                king_in_check = True
                                                break
                            if king_in_check:
                                break
                    if king_in_check:
                        # Checkmate detection: if the king in check has no legal moves, end the game
                        if not self.has_any_legal_moves(check_color):
                            QMessageBox.critical(self, "Checkmate", f"{check_color.capitalize()} is checkmated! Game over.")
                            self.setDisabled(True)
                            return
                        else:
                            QMessageBox.critical(self, "Check", f"{check_color.capitalize()} king is now in check!")
                # --- End check detection ---

                QMessageBox.information(self, "Moved", f"Moved to ({row}, {col})")
                GameBoard.turnVar = not GameBoard.turnVar
            else:
                QMessageBox.warning(self, "Invalid Move", "That move is not allowed.")

            self.selected_pos = None

