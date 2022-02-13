from board import Board as bb
from constants import Color, Piece

class Position:
   # the initial state
    def __init__(self):
        self.board = None
        self.to_move = Color.WHITE
        self.castle_rights = { Color.WHITE: True, Color.BLACK: True }
        self.en_passant_target = None
        self.halfmove_clock = 0

        self.piece_map = {}

    def get_piece_location(self):
        pass

    def set_initial_piece_locs(self):
        for i in range(8, 16):
            self.piece_map[i] = Piece.wP

        self.piece_map[0] = Piece.wR
        self.piece_map[7] = Piece.wR
        self.piece_map[1] = Piece.wN
        self.piece_map[6] = Piece.wN
        self.piece_map[2] = Piece.wB
        self.piece_map[5] = Piece.wB
        self.piece_map[3] = Piece.wQ
        self.piece_map[4] = Piece.wK

        for i in range(48, 56):
            self.piece_map[i] = Piece.wP

        self.piece_map[56] = Piece.bR
        self.piece_map[63] = Piece.bR
        self.piece_map[57] = Piece.bN
        self.piece_map[62] = Piece.bN
        self.piece_map[58] = Piece.bB
        self.piece_map[61] = Piece.bB
        self.piece_map[59] = Piece.bQ
        self.piece_map[60] = Piece.bK

        for i in range(48, 56):
            self.black_P_bb[i] = 1




    def make_move(self, move):
        self.to_move = not self.to_move
        if not self.is_legal_move(move):
            print('Illegal move')

            
        self.update_bitboards(move)

    def update_bitboards(self):
        pass


