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
            sorted_combo = sorted(list(combo))
            
            # super -> ctrl (only if ctrl not present)
            if "super" in sorted_combo and "ctrl" not in sorted_combo:
                src_mods = "+".join(sorted_combo)
                dst_mods = "+".join([m if m != "super" else "ctrl" for m in sorted_combo])
                for key in keys:
                    print(f"map {src_mods}+{key} send_key {dst_mods}+{key}")

            # ctrl -> super (only if super not present)
            if "ctrl" in sorted_combo and "super" not in sorted_combo:
                src_mods = "+".join(sorted_combo)
                dst_mods = "+".join([m if m != "ctrl" else "super" for m in sorted_combo])
                for key in keys:
                    print(f"map {src_mods}+{key} send_key {dst_mods}+{key}")
