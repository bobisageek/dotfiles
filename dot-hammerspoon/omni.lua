local exec = require("exec")

local super = {"ctrl"}
local sucon = {"ctrl", "cmd"}

-- pass a list of arguments to omniwmctl
local function omniL(...)
  local omnipath = '/opt/homebrew/bin/omniwmctl'
  local task = hs.task.new(omnipath, function(code, stdout, stderr)
    if code ~= 0 then
      hs.alert.show("omniwmctl error: " .. stderr)
    end
  end, {...})
  task:start()
  return task
end

-- split the string on spaces and pass the resulting list to omniL
local function omni(cmd)
  local args = {}
  for word in cmd:gmatch("%S+") do
    table.insert(args, word)
  end
  return omniL(table.unpack(args))
end

-- vim keybindings for focus and move windows
hs.hotkey.bind(super, "h", function() omni("command focus left") end)
hs.hotkey.bind(super, "j", function() omni("command focus-window-or-workspace-down") end)
hs.hotkey.bind(super, "k", function() omni("command focus-window-or-workspace-up") end)
hs.hotkey.bind(super, "l", function() omni("command focus right") end)
hs.hotkey.bind(sucon, "h", function() omni("command move-column left") end)
hs.hotkey.bind(sucon, "j", function() omni("command move down") end)
hs.hotkey.bind(sucon, "k", function() omni("command move up") end)
hs.hotkey.bind(sucon, "l", function() omni("command move-column right") end)
