import board
from kb import KMKKeyboard
from kmk.modules.split import Split

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord
from kmk.modules.modtap import ModTap
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.capsword import CapsWord


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
capsword = CapsWord()

modtap.tap_time = 200

# Custom definitions
## Aliases
NONE = KC.NO
TRNS = KC.TRNS

## Layer Aliases
AL1  = KC.MO(0)
AL2  = KC.MO(1)
SM1  = KC.MO(2)
SM2  = KC.MO(3)
NM1  = KC.MO(4)
SYS  = KC.MO(5)
BT   = KC.MO(6)
AL2U = KC.MO(7)
IMG  = KC.MO(8)

## Modifier Definitions
LCTL = KC.MT(KC.L, KC.LCTRL)
GALT = KC.MT(KC.G, KC.LALT)
DGUI = KC.MT(KC.D, KC.LGUI)
SSM2 = KC.LT(KC.S, SM2)
RSM1 = KC.LT(KC.R, SM1)
TSYS = KC.LT(KC.T, SYS)
INUM = KC.LT(KC.I, NM1)
SMEH = KC.MT(KC.SPC, KC.MEH)
#RPT = 
HGUI = KC.MT(KC.H, KC.RGUI)
UALT = KC.MT(KC.U, KC.RALT)
OCTL = KC.MT(KC.O, KC.RCTRL)
NSYS = KC.LT(KC.N, SYS)
ESM1 = KC.LT(KC.E, SM1)
ASM2 = KC.LT(KC.A, SM2)
CNUM = KC.LT(KC.C, NM1)
CTLD = KC.MT(KC.DOT, KC.LCTRL)
ALT0 = KC.MT(KC.KP_0, KC.LALT)
GUI1 = KC.MT(KC.KP_1, KC.LGUI)
GUI2 = KC.MT(KC.KP_2, KC.RGUI)
ALT3 = KC.MT(KC.KP_3, KC.RALT)
CTL4 = KC.MT(KC.KP_4, KC.RCTRL)



combos.combos = [
    Chord((HGUI, UALT, OCTL), SYS),
    Chord((SYS, SM1, SM2), KC.CW),
    
]

# Keymap
keyboard.modules = [split, layers, modtap, combos, capsword]
keyboard.extensions = [media]

keyboard.keymap = [
    # [ # AL1
    #     NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
    #     NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
    #     TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
    #                             TEST,   TEST,   TEST,   TEST
    # ]
    [ # AL1
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # AL2
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # SM1
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # SM2
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # NM1
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # SYS
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # BT
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ],
    [ # AL2U
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        NONE,   TEST,   TEST,   TEST,   NONE,   NONE,   TEST,   TEST,   TEST,  NONE,
        TEST,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,   NONE,  TEST,
                                TEST,   TEST,   TEST,   TEST
    ]
]

# GO GO GO
if __name__ == "__main__":
    keyboard.go()
