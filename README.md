# CSBLOCKS (Console Blocks)

Draw on terminal using Unicode block elements

Created as an exercise to learn __Python__ :muscle:

![Demo](images/demo.gif "Demo")

# How to run

You only need the csblocks.py file.

```python
from csblocks import Grid
# Create an instance
grid = Grid()
# Draw a block at (4, 2) (row 4, column 2)
grid.set(4, 2)
# Display
print grid
```

To run the demo (this project):

```
python example/main.py
```

Or with [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):

```
. bin/activate
python example/main.py

# turn off
deactivate
```

For details, see the __src/services/visualizer.py__ file.
