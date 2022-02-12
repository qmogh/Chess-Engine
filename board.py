import numpy as np
from pyrsistent import v

class Board:
    # ROOK
    # KNIGHT
    # BISHOP
    # QUEEN
    # KING
    # PAWN


    def __init__(self):
        pass
        self.white_rook_bitboard = self.create_empty_bitmap()
        self.white_king_bitboard = self.create_empty_bitmap()
        self.white_bishop_bitboard = self.create_empty_bitmap()
        self.white_pawn_bitboard = self.create_empty_bitmap()
        self.white_knight_bitboard = self.create_empty_bitmap()
        self.white_queen_bitboard = self.create_empty_bitmap()
       

        self.black_rook_bitboard = self.create_empty_bitmap()
        self.black_king_bitboard = self.create_empty_bitmap()
        self.black_bishop_bitboard = self.create_empty_bitmap()
        self.black_pawn_bitboard = self.create_empty_bitmap()
        self.black_knight_bitboard = self.create_empty_bitmap()
        self.black_queen_bitboard = self.create_empty_bitmap()
       
        self.initialize_pieces()

    def get_bitboard_state(self):
        return self.white_rook_bitboard \
            & self.white_king_bitboard \
            & self.white_pawn_bitboard \
            & self.white_bishop_bitboard \
            & self.white_knight_bitboard \
            & self.white_queen_bitboard \
            & self.black_king_bitboard \
            & self.black_pawn_bitboard \
            & self.black_bishop_bitboard \
            & self.black_knight_bitboard \
            & self.black_queen_bitboard \



    def create_empty_bitmap(self):
        return 64 *[0]

    def initialize_pieces(self):
        self.white_rook_bitboard[0] = 1
        self.white_rook_bitboard[7] = 1
        self.white_knight_bitboard[1] = 1
        self.white_knight_bitboard[6]=1
        self.white_bishop_bitboard[2] = 1
        self.white_bishop_bitboard[5] = 1
        self.white_queen_bitboard[4] = 1
        self.white_king_bitboard[4] = 1

        for i in range(8, 15):
            self.white_pawn_bitboard[i] = 1

        self.black_rook_bitboard[63] = 1
        self.black_rook_bitboard[56] = 1
        self.black_knight_bitboard[57] = 1
        self.black_knight_bitboard[62] =1

        self.black_bishop_bitboard[61] = 1
        self.black_bishop_bitboard[58] = 1
        self.black_queen_bitboard[59] = 1
        self.black_king_bitboard[60] = 1

        for i in range(8, 15):
            self.black_pawn_bitboard[i] = 1

        







    
