from os import getenv

if getenv("KITTY_OS") == "macos":
  for x in range(ord('a'), ord('z') + 1):
    print("map super+" + chr(x), "send_key ctrl+" + chr(x))
