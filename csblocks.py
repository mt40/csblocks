def array_init(len, default_value=None):
  if len < 0:
    return None
  return [default_value] * len

def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack(
      'HHHH', 
      fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return (w, h)

"""
Use unicode characters in the Block Elements group
(0x2580 -> 0x259F)
Another way is to use the Braille group

Mask is
1 | 2
-----
8 | 4
"""

mask = [[1, 2], [8, 4]]
char_map = {
  1: 0x98, 2: 0x9d, 4: 0x97, 8: 0x96,
  3: 0x80, 6: 0x90, 12: 0x84, 9: 0x8c,
  7: 0x9c, 14: 0x9f, 13: 0x99, 11: 0x9b,
  5: 0x9a, 10: 0x9e,
  15: 0x88
}
unicode_offset = 0x2500

cols = terminal_size()[0]

def char_for(code, encoding):
  """
  Return a ascii character corresponding to the unicode hex
  code -- unicode hex code
  """
  return unichr(unicode_offset | char_map[code]).encode(encoding)

class Grid:
  grid = []

  def __init__(self, rows=0):
    # Fill grid with False
    self.expand(rows)

  def set(self, y, x):
    """Set a cell at (x, y)"""
    r, c = self.index_for(y, x)

    # values our of range
    if cols <= x or x < 0 or y < 0:
      return

    # y is too big, expand the grid
    if len(self.grid) <= r:
      self.expand(r + 1)

    self.grid[r][c] |= mask[y % 2][x % 2]

    return self

  def unset(self, y, x):
    """Unset a cell at (x, y)"""
    r, c = self.index_for(y, x)
    
    # Values are out of range
    if cols <= x or x < 0 or y < 0 or len(self.grid) <= r:
      return

    self.grid[r][c] ^= mask[y % 2][x % 2]

    return self

  def clear(self):
    self.grid = []
    self.expand(0)

  def index_for(self, y, x):
    return (y >> 1, x >> 1)

  def expand(self, new_rows):
    old = len(self.grid)
    if new_rows < old:
      return

    for i in range(new_rows - old):
      self.grid.append(array_init(cols, 0))

  def entries_list(self, encoding='utf-8'):
    """
    Return a list of characters and their attributes. Each element
    is a tuple of (row, col, character, attribute)
    The returned row, col are the row and column of the console, not
    the internal coordinate of grid
    """
    rs = []
    for i in range(len(self.grid)):
      row = self.grid[i]
      for j in range(len(row)):
        code = row[j]
        char = char_for(code, encoding) if code > 0 else ' '
        rs.append((i, j, char))
    return rs

  def to_string(self, encoding='utf-8'):
    rs = ''
    for row in self.grid:
      for cell in row:
        rs += char_for(cell, encoding) if cell > 0 else ' '
      rs += '\n'
    return rs

  def __str__(self):
    return self.to_string()
