def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack(
      'HHHH', 
      fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
    return (w, h)

def array_init(len, default_value=None):
  if len < 0:
    return None
  return [default_value] * len
