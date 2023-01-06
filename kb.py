import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP8, # fake first matrix col as it has quirky behaviour
        board.GP9, board.GP10, board.GP11, board.GP12, board.GP13,
        board.GP22, board.GP21, board.GP20, board.GP19, board.GP18,
    )
    row_pins = (board.GP14, board.GP15, board.GP16, board.GP17)
    diode_orientation = DiodeOrientation.COL2ROW

    coord_mapping = [ # skips first col
      1,  2,  3,  4,  5,    6,  7,  8,  9, 10,
     12, 13, 14, 15, 16,   17, 18, 19, 20, 21,
     23, 24, 25, 26, 27,   28, 29, 30, 31, 32,
             36, 37, 38,   39, 40, 41
    ]