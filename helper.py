from Pieces.bishops.black.black_bishop import Black_Bishop
from Pieces.empty.empty import Empty_Spot
from Pieces.kings.black.black_king import Black_King
from Pieces.knights.black.black_knight import Black_Knight
from Pieces.pawns.black.black_pawn import Black_Pawn
from Pieces.queens.black.black_queen import Black_Queen
from Pieces.queens.white.white_queen import White_Queen
from Pieces.rooks.black.black_rook import Black_Rook
from board import Board
from Pieces.bishops.white.white_bishop import White_Bishop
from Pieces.kings.white.white_king import White_King
from Pieces.knights.white.white_knight import White_Knight
from Pieces.pawns.white.white_pawn import White_Pawn
from Pieces.rooks.white.white_rook import White_Rook


board_width = range(Board.getWIDTH())

#creates the pawns
def pawns(board, board_width):
    # Create white and black pawns with specific classes
    white_pawns = [White_Pawn(White_Pawn.get_piece_str()) for _ in board_width]
    black_pawns = [Black_Pawn(Black_Pawn.get_piece_str()) for _ in board_width]

    #places the white_pawns
    for i, pawn in enumerate(white_pawns):
        board.place_piece(pawn, i, 1)

    #places the black_pawns
    for i, pawn in enumerate(black_pawns):
        board.place_piece(pawn, i, 6)

# creates the rooks
def rooks(board, board_width):
    # Create white and black rooks with specific classes
    white_rooks = [White_Rook(White_Rook.get_piece_str()) for _ in board_width]
    black_rooks = [Black_Rook(Black_Rook.get_piece_str()) for _ in board_width]

    #places the white_rooks
    for i, rook in enumerate(white_rooks):
        if(i == 0) or (i == 7):
            board.place_piece(rook, i, 0)
            
    #places the black_rooks
    for i, rook in enumerate(black_rooks):
        if (i == 0) or (i == 7):
            board.place_piece(rook, i, 7)

#creates the kings
def kings(board, board_width):
    # Create white and black queens with specific classes
    white_kings = [White_King(White_King.get_piece_str()) for _ in board_width]
    black_kings = [Black_King(Black_King.get_piece_str()) for _ in board_width]

    #places the white_kings
    for i, king in enumerate(white_kings):
        if(i == 4):
            board.place_piece(king, i, 0)
            
    #places the black_kings
    for i, king in enumerate(black_kings):
        if (i == 4):
            board.place_piece(king, i, 7)

#creates the queenss
def queens(board, board_width):
    # Create white and black queens with specific classes
    white_queens = [White_Queen(White_Queen.get_piece_str()) for _ in board_width]
    black_queens = [Black_Queen(Black_Queen.get_piece_str()) for _ in board_width]

    #places the white_queens
    for i, queen in enumerate(white_queens):
        if(i == 3):
            board.place_piece(queen, i, 0)
            
    #places the black_queens
    for i, queen in enumerate(black_queens):
        if (i == 3):
            board.place_piece(queen, i, 7)

#creates the bishops
def bishops(board, board_width):
    # Create white and black bishops with specific classes
    white_bishops = [White_Bishop(White_Bishop.get_piece_str()) for _ in board_width]
    black_bishops = [Black_Bishop(Black_Bishop.get_piece_str()) for _ in board_width]

    #places the white_bishops
    for i, bishop in enumerate(white_bishops):
        if(i == 2) or (i == 5):
            board.place_piece(bishop, i, 0)
            
    #places the black_bishops
    for i, bishop in enumerate(black_bishops):
        if (i == 2) or (i == 5):
            board.place_piece(bishop, i, 7)

#creates the knights
def knights(board, board_width):
    # Create white and black rooks with specific classes
    white_knights = [White_Knight(White_Knight.get_piece_str()) for _ in board_width]
    black_knights = [Black_Knight(Black_Knight.get_piece_str()) for _ in board_width]

    #places the white_knights
    for i, knight in enumerate(white_knights):
        if(i == 1) or (i == 6):
            board.place_piece(knight, i, 0)
            
    #places the black_kings
    for i, knight in enumerate(black_knights):
        if (i == 1) or (i == 6):
            board.place_piece(knight, i, 7)
    
def empty_spots(board, board_width):
    # Create white and black rooks with specific classes
    empty_spots = [Empty_Spot(Empty_Spot.get_piece_str()) for _ in board_width]
    
    #places the white_pawns
    for i, pawn in enumerate(empty_spots):
        board.place_piece(pawn, i, 2)
    for i, pawn in enumerate(empty_spots):
        board.place_piece(pawn, i, 3)
    for i, pawn in enumerate(empty_spots):
        board.place_piece(pawn, i, 4)
    for i, pawn in enumerate(empty_spots):
        board.place_piece(pawn, i, 5)
    


            
# puts each piece on the board
def initialize_pieces(board, board_width):
    pawns(board, board_width)
    rooks(board, board_width)
    kings(board, board_width)
    queens(board, board_width)
    bishops(board, board_width)
    knights(board, board_width)
    empty_spots(board, board_width)

    