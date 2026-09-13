return {
  nu = function(script, callback)
  local nuPath = "/opt/homebrew/bin/nu"
  local task = hs.task.new(nuPath, function(code, stdout, stderr)
    if callback then callback(code, stdout, stderr) end
  end, {"-l", "-c", script})

  task:start()
  return task
end

}
