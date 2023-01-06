from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot


keyboard = KMKKeyboard()

layers = Layers()
mediakeys = MediaKeys()
mousekeys = MouseKeys()
modtap = ModTap()
oneshot = OneShot()

keyboard.modules = [layers, mediakeys, modtap, oneshot]

# OneShot mods
OS_LGUI = KC.OS(KC.LGUI, tap_time=None)
OS_LALT = KC.OS(KC.LALT, tap_time=None)
OS_LSFT = KC.OS(KC.LSFT, tap_time=None)
OS_LCTL = KC.OS(KC.LCTL, tap_time=None)
OS_RCTL = KC.OS(KC.RCTL, tap_time=None)
OS_RSFT = KC.OS(KC.RSFT, tap_time=None)
OS_RALT = KC.OS(KC.RALT, tap_time=None)
OS_RGUI = KC.OS(KC.RGUI, tap_time=None)

# Shortcuts
UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
REDO = KC.LCTL(KC.LSFT(KC.Z))
STAB = KC.LSFT(KC.TAB)
SAVE = KC.LCTRL(KC.S)
LOCK = KC.LWIN(KC.L)

# Layers
TAB_NAV = KC.LT(2, KC.TAB, prefer_hold = True)
CTL_NUM = KC.LT(3, KC.OS(KC.LCTL), prefer_hold = True)
LOCK_SYM1 = KC.LT(4, LOCK, prefer_hold = True)
ESC_SYM2 = KC.LT(5, KC.ESC, prefer_hold = True)
ESC_SYM3 = KC.LT(6, KC.ESC, prefer_hold = True)
ENT_MDA = KC.Ll(7, KC.ENTER, prefer_hold = True)

# Mod taps
SPC_SH = KC.MT(KC.SPACE, KC.LSHIFT, tap_interrupted=True)
BSPC_SH = KC.MT(KC.BSPACE, KC.RSHIFT, tap_interrupted=True)
DEL_SH = KC.MT(KC.DEL, KC.RSHIFT, tap_interrupted=True)
US_SH = KC.MT(KC.UNDS, KC.RSHIFT, tap_interrupted=True)
ZERO_SH = KC.MT(KC.N0, KC.RSHIFT, tap_interrupted=True)


TRACK = KCrMO(8) # For trackball, later
CANT = KC.NO # Impossible (do not map this)

keyboard.keymap = [
    [   # 0 - QWERTY
        KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,
        KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,
                                TAB_NAV,    SPC_SH,     CTL_NUM,            ENT_MDA,    BSPC_SH,    TRACK,
    ],
    [   # 1 - COLEMAK-DH
        KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,               KC.J,       KC.L,       KC.U,       KC.Y,       KC.SCLN,
        KC.A,       KC.R,       KC.S,       KC.T,       KC.G,               KC.M,       KC.N,       KC.E,       KC.I,       KC.O,
        KC.Z,       KC.X,       KC.D,       KC.V,       KC.Z,               KC.K,       KC.H,       KC.COMM,    KC.DOT,     KC.SLSH,
                                TAB_NAV,    SPC_SH,     CTL_NUM,            ENT_MDA,    BSPC_SH,    TRACK,
    ],
    [   # 2 - Nav
        KC.ESC,     KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.HOME,    KC.PGDN,    KC.PGUP,    KC.END,     KC.NO,  
        OS_LGUI,    OS_LALT,    OS_LSFT,    OS_LCTL,    KC.NO,              KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.DEL,
        UNDO,       CUT,        COPY,       PASTE,      REDO,               KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
                                CANT,       CANT,       CANT,               LOCK,       DEL_SH,     TRACK,              
    ],
    [   # 3 - Num
        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,  
        OS_LGUI,    OS_LALT,    OS_LSFT,    OS_LCTL,    KC.NO,              KC.DLR,     KC.N4,      KC.N5,      KC.N6,      KC.PERC,
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.N1,      KC.N2,      KC.N3,      KC.NO,  
                                CANT,       CANT,       CANT,               KC.ESC,     ZERO_SH,    TRACK,
    ],
    [   # 4 - Sym1
        KC.TILD,    KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.CIRC,    KC.PIPE,    KC.EXLM,    KC.AMPR,    KC.COLN, 
        OS_LGUI,    OS_LALT,    OS_LSFT,    OS_LCTL,    KC.NO,              KC.GRV,     KC.LABK,    KC.EQL,     KC.RABK,    KC.QUOT,
        KC.NO,      KC.NO,      KC.RCBR,    KC.RPRN,    KC.RBRC,            KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.QUES,  
                                CANT,       CANT,       CANT,               KC.NO,      US_SH,      TRACK,
    ],
    [   # 5 - Sym2
        KC.TILD,    KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.CIRC,    KC.PIPE,    KC.EXLM,    KC.AMPR,    KC.COLN, 
        OS_LGUI,    OS_LALT,    OS_LSFT,    OS_LCTL,    KC.NO,              KC.GRV,     KC.LABK,    KC.EQL,     KC.RABK,    KC.QUOT,
        KC.NO,      KC.NO,      KC.RCBR,    KC.RPRN,    KC.RBRC,            KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.QUES,  
                                CANT,       CANT,       CANT,               STAB,       KC.EXLM,    TRACK,            
    ],
    [   # 6 - Sym3
        KC.TILD,    KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.CIRC,    KC.PIPE,    KC.EXLM,    KC.AMPR,    KC.COLN, 
        OS_LGUI,    OS_LALT,    OS_LSFT,    OS_LCTL,    KC.NO,              KC.GRV,     KC.LABK,    KC.EQL,     KC.RABK,    KC.QUOT,
        KC.NO,      KC.NO,      KC.RCBR,    KC.RPRN,    KC.RBRC,            KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.QUES,  
                                CANT,       CANT,       CANT,               STAB,       US_SH,      TRACK,            
    ],
    [   # 7 - Media
        KC.DF(0),   KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.BRID,    KC.BRIU,    KC.NO,      KC.DF(1),  
        KC.NO,      KC.MPRV,    KC.MPLY,    KC.MNXT,    KC.NO,              KC.MUTE,    KC.VOLD,    KC.VOLU,    KC.MUTE,    KC.NO,
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
                                LOCK_SYM1,  ESC_SYM2,   ESC_SYM3,           CANT,       CANT,       TRACK,
    ],
    [   # 8 - Mouse
        KC.NO,      KC.NO,      KC.MS_UP,   KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.MB_MMB,  KC.NO,      KC.NO,  
        KC.NO,      KC.MS_LT,   KC.MS_DN,   KC.MS_RT,   KC.NO,              KC.NO,      KC.MB_LMB,  KC.MB_RMB,  KC.NO,      KC.NO,  
        KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,              KC.NO,      KC.NO,      KC.NO,      KC.NO,      KC.NO,  
                                KC.NO,      KC.NO,      KC.NO,              CANT,       CANT,       CANT,
    ],
]

if __name__ == '__main__':
    keyboard.go()
