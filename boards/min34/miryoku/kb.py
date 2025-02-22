import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
    row_pins = (board.D10, board.D9, board.D8, board.D7)
    diode_orientation = DiodeOrientation.COL2ROW

    coord_mapping = [
         0,  1,  2,  3,  4, 24, 23, 22, 21, 20,
         5,  6,  7,  8,  9, 29, 28, 27, 26, 25,
        10, 11, 12, 13, 14, 34, 33, 32, 31, 30,
                    18, 19, 39, 38
    ]
