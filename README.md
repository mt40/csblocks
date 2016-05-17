# CSBLOCKS (Console Blocks)

Draw on terminal using Unicode block elements

Created as an exercise to learn __Python__ :muscle:

![Demo](images/demo.gif "Demo")

# How to run

You only need the __csblocks.py__ file.

```python
from csblocks import Grid
# Create an instance
grid = Grid()
# Draw a block at (4, 2) (row 4, column 2)
grid.set(4, 2)
# Display
print grid
```

To run the example:

```
python example.py
```

Or with [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):

```
. bin/activate
python example.py

# turn off
deactivate
```

For details, see the __example.py__ file.
