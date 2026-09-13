return {
  menuMap = {
    -- Press 'r' inside the menu to reload the configuration
    [{{}, "r", "Reload Config"}] = function()
        hs.reload()
    end,

    -- Press 'c' inside the menu to show the Hammerspoon console
    [{{}, "c", "Show Console"}] = function()
        hs.toggleConsole()
    end
}
}
