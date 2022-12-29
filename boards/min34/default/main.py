import board
from kb import KMKKeyboard
from kmk.modules.split import Split

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

# Firmware setup
keyboard = KMKKeyboard()

split = Split(
    data_pin = board.D6,
    use_pio = True,
    split_flip = True
)

# Keymap configuration
layers = Layers()
modtap = ModTap()

keyboard.modules = [split, layers, modtap]

# Aliases
keyboard.keymap = [
    [ # base layer
       KC.Q,    KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,
       KC.A,    KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,   KC.QUOT,
       KC.Z,    KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,
                                KC.BSPC,KC.ENT, KC.TAB, KC.SPC 
    ]
]

if __name__ == "__main__":
    keyboard.go()