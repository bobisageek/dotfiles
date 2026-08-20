from os import getenv
import itertools
import sys

if getenv("KITTY_OS") == "macos" or sys.argv.__len__()> 1:
    keys = []
    # Lowercase letters
    keys.extend([chr(x) for x in range(ord('a'), ord('z') + 1)])
    # Digits
    keys.extend([chr(x) for x in range(ord('0'), ord('9') + 1)])
    # Symbols
    keys.extend([';', "'", '[', ']', '\\', ',', '.', '/', '-', '='])
    # Navigation/Editing
    keys.extend(['home', 'end', 'page_up', 'page_down', 'insert', 'delete'])
    # Function keys
    keys.extend([f'f{i}' for i in range(1, 13)])
    # Other keys
    keys.extend(['tab', 'enter', 'space', 'backspace', 'escape', 'up', 'down', 'left', 'right'])

    mods_pool = ["ctrl", "shift", "alt", "super"]

    # Generate all combinations of modifiers
    for r in range(1, len(mods_pool) + 1):
        for combo in itertools.combinations(mods_pool, r):
            # Must contain super, but not both super and ctrl
            if "super" in combo and "ctrl" not in combo:
                # Sort modifiers consistently (optional but cleaner)
                sorted_combo = sorted(list(combo))
                src_mods = "+".join(sorted_combo)
                dst_mods = "+".join([m if m != "super" else "ctrl" for m in sorted_combo])

                for key in keys:
                    print(f"map {src_mods}+{key} send_key {dst_mods}+{key}")
