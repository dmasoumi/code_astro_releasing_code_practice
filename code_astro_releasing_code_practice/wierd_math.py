import numpy as np

def wierd_sum(x, y):
  z = np.abs(x+y) + np.abs(x-y)
  return z

def wierd_substract(x, y):
  z = np.abs(x+y) - np.abs(x-y)
  return z
