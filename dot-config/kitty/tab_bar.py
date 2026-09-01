# vim: set shiftwidth=2 tabstop=2 expandtab:

from kitty.fast_data_types import Screen, get_options, get_boss
from kitty import tab_bar
from kitty.tab_bar import (DrawData, ExtraData, TabBarData, as_rgb)
from kitty.utils import color_as_int

tab_styler = tab_bar.draw_tab_with_powerline

mode_keys = {
  '': 'alt+space/w/s',
  'manage': 'w/t/s',
  'tab': 'r/n/x/h/l/m',
  'move_tab': 'h/l',
  'window': "r/n/v/s/x/h/l/'/'/=",
  'move_window': 'h/l/s',
  'resize_window': 'h/l/j/k/H/L/J/K',
  'scroll': 'j/k/pgup/pgdn/home/end',
}

def draw_tab(
  draw_data: DrawData,
  screen: Screen,
  tab: TabBarData,
  before: int,
  max_title_length: int,
  index: int,
  is_last: bool,
  extra_data: ExtraData,
  ) -> int:
  """Draw a single tab in the tab bar, with mode on the right"""
  mode = get_boss().mappings.current_keyboard_mode_name
  # Draw the tab with powerline style
  end = tab_styler(
    draw_data,
    screen,
    tab,
    before,
    max_title_length,
    index,
    is_last,
    extra_data,
    )

  if is_last:
    setup_cursor(draw_data, screen)
    text_to_put = compute_text(mode, screen.columns - (end + 1))
    if text_to_put:
      screen.cursor.x = screen.columns - len(text_to_put)
      screen.draw(text_to_put)

  return end

def setup_cursor(draw_data: DrawData, screen: Screen) -> None:
  screen.cursor.fg = as_rgb(color_as_int(draw_data.inactive_fg))
  screen.cursor.bg = as_rgb(color_as_int(draw_data.inactive_bg))
  screen.cursor.bold = False
  screen.cursor.italic = False
  screen.cursor.blink = False

def compute_text(mode: str, width: int) -> str:
  keys = mode_keys.get(mode, '')
  if width <= 0 or not keys:
    return ''
  return keys[:width - 1] + '' if len(keys) > width else keys
