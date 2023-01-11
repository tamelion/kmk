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

# Navigation
TABP = KC.LCTL(KC.PGUP)
TABN = KC.LCTL(KC.PGDN)

# Layers
SPC_NAV = KC.LT(2, KC.SPACE, prefer_hold=True)
ENT_SYM= KC.LT(3, KC.ENT, prefer_hold=True)
TAB_NUM= KC.LT(4, KC.TAB, prefer_hold=True)
SWF_EXT = KC.LT(5, KC.NO, prefer_hold=True)

# Mod taps
BSPC_SH = KC.MT(KC.BSPACE, KC.RSHIFT)
ZERO_SH = KC.MT(KC.N0, KC.RSHIFT)

TRACK = KC.MO(6) # For trackball, later
CANT = KC.NO # Impossible (do not map this)

combos.combos = [
    Sequence((KC.COMM, KC.J), KC.ESC, timeout=200),
    #Chord((KC.L, KC.QUOT), KC.ENT),

    # LHS
    Chord((12,13), KC.LGUI, match_coord=True),
    Chord((13,14), KC.LALT, match_coord=True),
    Chord((14,15), KC.LCTL, match_coord=True),
    Chord((12,13,14), KC.LGUI(KC.LALT), match_coord=True),
    Chord((13,14,15), KC.LALT(KC.LCTL), match_coord=True),
    # RHS
    Chord((18,19), KC.RCTL, match_coord=True),
    Chord((19,20), KC.RALT, match_coord=True),
    Chord((20,21), KC.LGUI, match_coord=True),
    Chord((18,19,20), KC.RCTL(KC.RALT), match_coord=True),
    Chord((19,20,21), KC.RALT(KC.LGUI), match_coord=True),

    Chord((KC.COMMA, KC.DOT), KC.EXLM),
    Chord((KC.DOT, KC.SLSH), KC.COLN),
]


keyboard.keymap = [
    [   # 0 - QWERTY
        KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,
        KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.QUOT,
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,
                                TAB_NUM,    SPC_NAV,    TRACK,              KC.NO,      BSPC_SH,    ENT_SYM,
    ],
    [   # 1 - COLEMAK-DH
        KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,               KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,
        KC.A,       KC.R,       KC.S,       KC.T,       KC.G,               KC.M,       KC.N,       KC.E,       KC.I,       KC.O,
        KC.Z,       KC.X,       KC.D,       KC.V,       KC.Z,               KC.K,       KC.H,       KC.COMM,    KC.DOT,     KC.SLSH,
                                TAB_NUM,    SPC_NAV,    TRACK,              KC.NO,      BSPC_SH,    ENT_SYM,
    ],
    [   # 2 - Nav
        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,  
        KC.TILD,    KC.HOME,    TABP,       TABN,       KC.END,             KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.SCLN,
        UNDO,       CUT,        COPY,       PASTE,      REDO,               KC.MINS,    KC.EQL,     KC.LBRC,    KC.RBRC,    KC.BSLS,  
                                CANT,       CANT,       CANT,               KC.NO,      KC.NO,      KC.NO,
    ],
    [   # 3 - Sym 
        KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,            KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.MINS,    KC.PLUS, 
        KC.TILD,    KC.LBRC,    KC.LCBR,    KC.LPRN,    KC.NO,              KC.GRV,     KC.RPRN,    KC.RCBR,    KC.RBRC,    KC.COLN,
        KC.NO,      KC.LABK,    KC.EQL,     KC.RABK,    KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.QUES,  
                                SWF_EXT,    KC.UNDS,    TRACK,              CANT,       CANT,       CANT,
    ],
    [   # 4 - Num
        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,  
        KC.PSLS,    KC.PMNS,    KC.PPLS,    KC.PAST,    KC.EQL,             KC.DLR,     KC.N4,      KC.N5,      KC.N6,      KC.EQL,
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.N1,      KC.N2,      KC.N3,      KC.DOT,  
                                CANT,       CANT,       CANT,               TRACK,      KC.N0,      SWF_EXT,
    ],
    [   # 5 - Ext
        KC.DF(0),   KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.BRID,    KC.BRIU,    KC.NO,      KC.DF(1),  
        KC.NO,      KC.MPRV,    KC.MPLY,    KC.MNXT,    KC.NO,              KC.MUTE,    KC.VOLD,    KC.VOLU,    KC.MUTE,    KC.NO,
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
                                CANT,       CANT,       CANT,               CANT,       CANT,       TRACK,
    ],
    [   # 6 - Mouse
        KC.NO,      KC.NO,      KC.MS_UP,   KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.MB_MMB,  KC.NO,      KC.NO,  
        KC.NO,      KC.MS_LT,   KC.MS_DN,   KC.MS_RT,   KC.NO,              KC.NO,      KC.MB_LMB,  KC.MB_RMB,  KC.NO,      KC.NO,  
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
                                KC.NO,      KC.NO,      KC.NO,              CANT,       CANT,       CANT,
    ],
]

if __name__ == '__main__':
    keyboard.go()
