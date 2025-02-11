from keycodes.keycodes import Keycode
from keymap import brazilian, canadian_csa, danish, french, german, hebrew, hungarian, japanese, latam, norwegian, russian, slovak, spanish, swedish, swedish_swerty, swiss, croatian

KEYMAPS = [
    ("QWERTY", dict()),
    ("Brazilian (QWERTY)", brazilian.keymap),
    ("Canadian CSA (QWERTY)", canadian_csa.keymap),
    ("Croatian (QWERTZ)", croatian.keymap),
    ("Danish (QWERTY)", danish.keymap),
    ("French (AZERTY)", french.keymap),
    ("French (MAC)", french.keymap_mac),
    ("German (QWERTZ)", german.keymap),
    ("Hebrew (Standard)", hebrew.keymap),
    ("Hungarian (QWERTZ)", hungarian.keymap),
    ("Japanese (QWERTY)", japanese.keymap),
    ("Latin American (QWERTY)", latam.keymap),
    ("Norwegian (QWERTY)", norwegian.keymap),
    ("Russian (ЙЦУКЕН)", russian.keymap),
    ("Slovak (QWERTY)", slovak.keymap),
    ("Spanish (QWERTY)", spanish.keymap),
    ("Swedish (QWERTY)", swedish.keymap),
    ("Swedish (SWERTY)", swedish_swerty.keymap),
    ("Swiss (QWERTZ)", swiss.keymap)
]

# make sure that qmk IDs we used are all correct
for name, keymap in KEYMAPS:
    for qmk_id in keymap.keys():
        if Keycode.find_by_qmk_id(qmk_id) is None:
            raise RuntimeError("Misconfigured - cannot find QMK keycode {}".format(qmk_id))
