import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.split import Split, SplitSide
from storage import getmount


keyboard = _KMKKeyboard()

# 000 001 002 003 004 024 023 022 021 020 
# 005 006 007 008 009 029 028 027 026 025 
# 010 011 012 013 014 034 033 032 031 030 
#             018 019 039 038 

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
    row_pins = (board.D10, board.D9, board.D8, board.D7)
    diode_orientation = DiodeOrientation.COL2ROW

keyboard = KMKKeyboard()

split = Split(
    data_pin=board.D6,
    split_flip=True,
    use_pio=True
)

keyboard.modules.append(split)

# keyboard.keymap = [
#     [KC.A,]
# ]

# *2 for split keyboards, which will typically manage twice the number of keys
# of one side. Having this N too large will have no impact (maybe slower boot..)
N = len(keyboard.col_pins) * len(keyboard.row_pins) * 2

keyboard.coord_mapping = list(range(N))

layer = []

for i in range(N):
    c, r = divmod(i, 100)
    d, u = divmod(r, 10)
    layer.append(
        simple_key_sequence(
            (
                getattr(KC, 'N' + str(c)),
                getattr(KC, 'N' + str(d)),
                getattr(KC, 'N' + str(u)),
                KC.SPC,
            )
        )
    )
keyboard.keymap = [layer]

if __name__ == '__main__':
    keyboard.go()
if __name__ == '__main__':
    keyboard.go()