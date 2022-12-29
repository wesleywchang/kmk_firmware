import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.split import Split, SplitSide, SplitType
from storage import getmount


keyboard = _KMKKeyboard()

# ['__class__', '__name__', 'A0', 'A1', 'A2', 'A3', 'D0', 'D1', 'D10', 'D2',
#  'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'I2C', 'LED', 'LED_BLUE', 'LED_GREEN',
#   'LED_RED', 'MISO', 'MOSI', 'NEOPIXEL', 'NEOPIXEL_POWER', 'RX', 'SCK', 'SCL',
#    'SDA', 'SPI', 'TX', 'UART', 'board_id']

#side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

class KMKKeyboard(_KMKKeyboard):
#    if side == SplitSide.RIGHT:
#        col_pins = (board.D4, board.D3, board.D2, board.D1, board.D0)
#    else:
    col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
    row_pins = (board.D10, board.D9, board.D8, board.D7)
    diode_orientation = DiodeOrientation.COL2ROW

keyboard = KMKKeyboard()

split = Split(
    data_pin=board.D6,
#    data_pin2=board.D6,
    split_target_left=True,
    split_type=SplitType.UART,
    split_side=SplitSide.LEFT,
#    split_flip=True,
    use_pio=True
#    uart_flip=True
)

#if side == SplitSide.RIGHT:
#    split.data_pin = board.D6
#    split.data_pin2 = board.D2

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