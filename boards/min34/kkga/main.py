import board
from kb import KMKKeyboard
from kmk.modules.split import Split

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord
from kmk.modules.modtap import ModTap
from kmk.extensions.media_keys import MediaKeys


# Firmware setup
keyboard = KMKKeyboard()

# Turn this on for debugging
# keyboard.debug_enabled = True


split = Split(
    data_pin = board.D6,
    use_pio = True,
    split_flip = True
)

# Keymap configuration
layers = Layers()
modtap = ModTap()
combos = Combos()
media = MediaKeys()

modtap.tap_time = 200

# Custom definitions
## Aliases
NONE = KC.NO
TRNS = KC.TRNS

## Home Row Mods
LSFT = KC.MT(KC.F, KC.LSFT)
LCTL = KC.MT(KC.D, KC.LCTRL)
LALT = KC.MT(KC.S, KC.LALT)
LGUI = KC.MT(KC.A, KC.LGUI)
RSFT = KC.MT(KC.J, KC.RSFT)
RCTL = KC.MT(KC.K, KC.RCTRL)
RALT = KC.MT(KC.L, KC.RALT)
RGUI = KC.MT(KC.QUOT, KC.RGUI)

EXT = KC.MO(1)
SYM = KC.MO(2)
NUM = KC.MO(3)

combos.combos = [
    Chord((KC.W, KC.E), KC.ESC),
    Chord((KC.X, KC.C), KC.TAB),
    Chord((KC.I, KC.O), KC.BSPC),
    Chord((EXT, SYM), NUM)
]

# Keymap
keyboard.modules = [split, layers, modtap, combos]
keyboard.extensions = [media]

keyboard.keymap = [
    # [ # base layer - QWERTY
    #     KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,
    #     LGUI,   LALT,   LSFT,   LCTL,   KC.G,   KC.H,   RCTL,   RSFT,   RALT,   RGUI,
    #     KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,
    #                             KC.BSPC,KC.ENT, KC.TAB, KC.SPC
    # ],
    [ # QWERTY - layer 0
        KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,
        LGUI,   LALT,   LCTL,   LSFT,   KC.G,   KC.H,   RSFT,   RCTL,   RALT,   RGUI,
        KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,
                                EXT,    KC.SPC, KC.ENT, SYM
    ],
    [ # Extend - layer 1
        NONE,   NONE,   KC.VOLD,KC.VOLU,NONE,   KC.HOME,KC.PGDN,KC.PGUP,KC.END, NONE,
        KC.LGUI,KC.LALT,KC.LCTL,KC.LSFT,NONE,   KC.LEFT,KC.DOWN,KC.UP,  KC.RGHT,KC.BSPC,
        KC.ESC, NONE,   NONE,   KC.TAB, NONE,   NONE,   KC.ENT, NONE,   NONE,   KC.DEL,
                                TRNS,   NONE,   KC.ENT, NUM
    ],
    [ # Symbol - layer 2
        KC.EXLM,KC.AT,  KC.HASH,KC.DLR, KC.PERC,KC.CIRC,KC.AMPR,KC.ASTR,KC.UNDS,KC.SCLN,
        KC.GRV, KC.TILD,KC.LCBR,KC.LPRN,KC.LBRC,KC.COLN,KC.RSFT,KC.RCTL,KC.RALT,KC.RGUI,
        KC.LABK,KC.RABK,KC.RCBR,KC.RPRN,KC.RBRC,KC.PIPE,KC.PMNS,KC.PEQL,KC.PPLS,KC.BSLS,
                                NUM,    NONE,   NONE,   TRNS
    ],
    [ # Num - layer 3
        NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   KC.N7,  KC.N8,  KC.N9,  NONE,
        KC.LGUI,KC.LALT,KC.LCTL,KC.LSFT,NONE,   NONE,   KC.N4,  KC.N5,  KC.N6,  NONE,
        NONE,   NONE,   NONE,   NONE,   NONE,   KC.N0,  KC.N1,  KC.N2,  KC.N3,  NONE,
                                TRNS,   NONE,   NONE,   TRNS
    ]
]

# GO GO GO
if __name__ == "__main__":
    keyboard.go()
