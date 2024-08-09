from piece import Piece

class Black_Pawn(Piece):
    #overidden function for moving the Black_Pawn
    def move(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        if piece and str(piece) == 'BP':
            # Ensure it's a valid move
            if (from_y == 6 and to_y in [4, 5]) or (from_y != 6 and to_y == from_y - 1):
                if from_x == to_x and board.grid[to_y][to_x] is None:
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)
        return Piece.invalid_move()
    
    def take_piece(board, from_x, from_y, to_x, to_y):
        piece = board.grid[from_y][from_x]
        target = board.grid[to_y][to_x]
        
        # Ensure the piece is a black White_Pawn
        if piece and str(piece) == 'BP':
            # Check if the move is a valid diagonal move
            if (abs(from_x - to_x) == 1 and from_y - to_y == 1):
                # Ensure there is a white piece to capture
                if target and str(target).startswith('W'):
                    return Piece.valid_move(piece, board, from_x, from_y, to_x, to_y)           
        return Piece.invalid_move()
