local exec = require("exec")
local keys = require("keys")
local hs_menu = require("hs_menu")
local rb = hs.loadSpoon("RecursiveBinder")

hs.hotkey.bind({"ctrl"}, "/", function()
  local win = hs.window.focusedWindow()
  if not win then return end
  local frame = win:frame()
  local center = hs.geometry.point(frame.x + frame.w / 2, frame.y + frame.h / 2)
  hs.mouse.absolutePosition(center)
end)

hs.hotkey.bind({"ctrl"}, "Escape", function()
  exec.nu("switch_workspace")
end)

hs.hotkey.bind(keys.hyper, "h", rb.recursiveBind(hs_menu.menuMap))
