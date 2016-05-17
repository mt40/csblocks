import curses, time
from grid import Grid

# Fix curses encoding for Python 2
import locale
locale.setlocale(locale.LC_ALL, '')

class Visualizer:
  stdscr = None

  def _init(self):
    self.stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color() # enable color output

  def start(self, data, title, max_y=10, delay=0.3):
    self._init()
    try:
      self._run(data, title, max_y, delay)
    finally:
      self.end()

  def _run(self, data, title, max_y, delay):
    # The y coordinate in data is inverted (i.e. y=0 is at the top)
    # so we have to make it right
    max_y += 2

    grid = Grid(max_y + 1)
    
    for frame in data:
      # Clear screen
      self.stdscr.clear()
      self.stdscr.refresh()

      for x, y in frame:
        grid.set(max_y - y, x)
        for i in range(1, y):
          grid.set(max_y - i, x)

      entries = grid.entries_list()

      for r, c, char in entries:
        self.stdscr.addstr(r, c, char)

      # Add the title
      # Dont't know why but I have to subtract 5 to move it up
      self.stdscr.addstr(max_y - 5, 0, title)
      self.stdscr.refresh()

      time.sleep(delay)
      grid.clear()

  def end(self):
    """Must be called or terminal will not display typed text"""
    curses.nocbreak()
    self.stdscr.keypad(False)
    curses.echo()
    curses.endwin()
