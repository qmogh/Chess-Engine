from board import Board as bb
from constants import Color

class Position:
   # the initial state
    def __init__(self):
        self.board = None
        self.to_move = Color.WHITE
        self.castle_rights = { Color.WHITE: True, Color.BLACK: True }
        self.en_passant_target = None
        self.halfmove_clock = 0