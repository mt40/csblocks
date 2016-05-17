import sys, random, time
from src.services.grid import Grid
from src.services.visualizer import Visualizer
from src.helpers.utils import array_init

max_y = 10

def gen(n_frames, n_points):
  """
  Generate frames, each contains points with random y value
  n_frames -- Number of frames
  n_points -- Number of points
  """
  frames = array_init(n_frames)
  for i in range(n_frames):
    points = array_init(n_points) # initialize a list with size

    for j in range(n_points):
      y = random.randint(1, max_y)
      points[j] = [j, y] # [x,y] pair

    frames[i] = points
  return frames

if __name__ == '__main__':
  vs = Visualizer()
  vs.start(gen(30, 100), 'Playing', max_y, 0.3)
