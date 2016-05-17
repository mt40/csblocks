class Attr:
  """Attributes for text on console"""

  _attr = 0
  _curses = None

  def __init__(self, curses):
    self._curses = curses
    try:
      init_colors(curses)
    except:
      raise ValueError('Invalid "curses" instance')

  def bold(self):
    self._attr |= self._curses.A_BOLD
    return self

  def underline(self):
    self._attr |= self._curses.A_UNDERLINE
    return self

  def reverse(self):
    self._attr |= self._curses.A_REVERSE
    return self

  def dim(self):
    self._attr |= self._curses.A_DIM
    return self

  def color(self, color_id):
    """
    Add color atttribute
    color_id -- color constant from class Color
    e.g. Color.BLACK
    """
    self._attr |= self._curses.color_pair(color_id)
    return self

  def done(self):
    """Call after customization to get the complete attribute"""
    return self._attr

  def clear(self):
    self._attr = 0
    return self

class Color:
  BLACK = 1
  BLUE = 2
  CYAN = 3
  MAGENTA = 4
  RED = 5
  WHITE = 6
  YELLOW = 7

def init_colors(curses):
  black = curses.COLOR_BLACK
  curses.init_pair(Color.BLACK, curses.COLOR_BLACK, black)
  curses.init_pair(Color.BLUE, curses.COLOR_BLUE, black)
  curses.init_pair(Color.CYAN, curses.COLOR_CYAN, black)
  curses.init_pair(Color.MAGENTA, curses.COLOR_MAGENTA, black)
  curses.init_pair(Color.RED, curses.COLOR_RED, black)
  curses.init_pair(Color.WHITE, curses.COLOR_WHITE, black)
  curses.init_pair(Color.YELLOW, curses.COLOR_YELLOW, black)
