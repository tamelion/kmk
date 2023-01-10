from kb import KMKKeyboard

from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys

from kmk.modules.combos import Chord, Combos, Sequence
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

combos = Combos()
layers = Layers()
mediakeys = MediaKeys()
mousekeys = MouseKeys()
modtap = ModTap()

# Config for modtap and layertap
modtap.tap_time = 300
modtap.tap_interrupted = True
modtap.repeat = HoldTapRepeat.ALL

keyboard.modules = [combos, layers, mediakeys, modtap, mousekeys]

# Shortcuts
UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
REDO =KC.LCTL(KC.LSFT(KC.Z))
STAB = KC.LSFT(KC.TAB)
SAVE = KC.LCTRL(KC.S)
LOCK = KC.LWIN(KC.L)

# Layers
SPC_NAV = KC.LT(1, KC.SPACE)
TAB_SYM = KC.LT(3, KC.TAB)
SWB_NUM = KC.LT(4, KC.NO)
SWF_EXT = KC.LT(5, KC.NO)

# Mod taps
BSPC_SH = KC.MT(KC.BSPACE, KC.RSHIFT)
CMD_SH = KC.MT(KC.LCMD, KC.RSHIFT)
Z_SH = KC.MT(KC.Z, KC.LSHIFT)
SL_SH = KC.MT(KC.SLSH, KC.RSHIFT)
#US_SH = KC.MT(KC.UNDS, KC.RSHIFT)
ZERO_SH = KC.MT(KC.N0, KC.RSHIFT)

TRACK = KC.MO(2) # For trackball, later
CANT = KC.NO # Impossible (do not map this)

combos.combos = [
    Sequence((KC.COMM, KC.J), KC.ESC, timeout=200),
    #Chord((KC.L, KC.QUOT), KC.ENT),

    # LHS
    Chord((12,13), KC.LALT, match_coord=True),
    Chord((13,14), KC.LALT(KC.LCTL), match_coord=True),
    Chord((14,15), KC.LCTL, match_coord=True),

    # RHS
    Chord((18,19), KC.RCTL, match_coord=True),
    Chord((19,20), KC.RALT(KC.RCTL), match_coord=True),
    Chord((20,21), KC.RALT, match_coord=True),
]

keyboard.keymap = [
    [   # 0 - QWERTY
        KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,
        KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.QUOT,
        Z_SH,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     SL_SH,
                                KC.TAB,     SPC_NAV,    TRACK,              TRACK,      BSPC_SH,    KC.ENT,
    ],
#    [   # 1 - COLEMAK-DH
#        KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,               KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,
#        KC.A,       KC.R,       KC.S,       KC.T,       KC.G,               KC.M,       KC.N,       KC.E,       KC.I,       KC.O,
#        KC.Z,       KC.X,       KC.D,       KC.V,       KC.Z,               KC.K,       KC.H,       KC.COMM,    KC.DOT,     KC.SLSH,
#                                KC.TAB,     SPC_NAV,    TRACK,              TRACK,      BSPC_SH,    TRACK,
#    ],
    [   # 2 - Nav
        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,  
        KC.TILD,    KC.HOME,    KC.PGDN,    KC.PGUP,    KC.END,             KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.SCLN,
        UNDO,       CUT,        COPY,       PASTE,      REDO,               KC.MINS,    KC.EQL,     KC.LBRC,    KC.RBRC,    KC.BSLS,  
                                CANT,       CANT,       CANT,               TRACK,      BSPC_SH,    TRACK,
    ],
#    [   # 3 - Sym 
#        KC.TILD,    KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.CIRC,    KC.PIPE,    KC.EXLM,    KC.AMPR,    KC.COLN, 
#        KC.AT,      KC.HASH,    KC.LCBR,    KC.LPRN,    KC.LBRC,            KC.GRV,     KC.LABK,    KC.EQL,     KC.RABK,    KC.QUOT,
#        KC.NO,      KC.NO,      KC.RCBR,    KC.RPRN,    KC.RBRC,            KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.QUES,  
#                                CANT,       CANT,       CANT,               STAB,       KC.EXLM,    TRACK,
#    ],
#    [   # 4 - Num
#        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,  
#        KC.PSLS,    KC.PMNS,    KC.EQL,     KC.PPLS,    KC.PAST,            KC.DLR,     KC.N4,      KC.N5,      KC.N6,      KC.PERC,
#        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.N1,      KC.N2,      KC.N3,      KC.NO,  
#                                CANT,       CANT,       CANT,               KC.ESC,     ZERO_SH,    TRACK,
#    ],
#    [   # 5 - Ext
#        KC.DF(0),   KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.BRID,    KC.BRIU,    KC.NO,      KC.DF(1),  
#        KC.NO,      KC.MPRV,    KC.MPLY,    KC.MNXT,    KC.NO,              KC.MUTE,    KC.VOLD,    KC.VOLU,    KC.MUTE,    KC.NO,
#        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
#                                CANT,       CANT,       CANT,               CANT,       CANT,       TRACK,
#    ],
    [   # 6 - Mouse
        KC.NO,      KC.NO,      KC.MS_UP,   KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.MB_MMB,  KC.NO,      KC.NO,  
        KC.NO,      KC.MS_LT,   KC.MS_DN,   KC.MS_RT,   KC.NO,              KC.NO,      KC.MB_LMB,  KC.MB_RMB,  KC.NO,      KC.NO,  
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
                                KC.NO,      KC.NO,      KC.NO,              CANT,       CANT,       CANT,
    ],
]

if __name__ == '__main__':
    keyboard.go()
