from abc import ABCMeta, abstractmethod
import math

class Sequence(metaclass=ABCMeta): #note metaclass vs super
  @abstractmethod #decorator implies no implementation here but expected to implement for all subclasses
  def __len__(self):
    """docstring 1"""

  @abstractmethod
  def __getitem__(self, j):
    """docstring 2"""

  def __contains__(self, val):
    for j in range(len(self)):
      if self[j] == val:
        return True
    return False

  def index(self, val):
    for j in range(len(self)):
      if self[j] == val:
        return j
      raise ValueError('value not in sequence')

  def count(self, val):
    k = 0
    for j in range(len(self)):
      if self[j] == val:
        k += 1
    return k
  
class Range(Sequence):
  def __init__(self, start, stop=None, step=1):
    if step==0:
      raise ValueError("step cannot be 0")
    if stop is None:
      start, stop = 0, start
    plen = math.ceil(abs(stop-start)/abs(step))
    self._length = max(0, plen)
    # self._length = max(0, (stop-start+step-1)//step) #doesn't work for step<0
    self._start = start
    self._step = step

  def __len__(self):
    return self._length
  
  def __getitem__(self, k):
    if k < 0:
      k += len(self)
    if not 0 <= k < self._length:
      raise IndexError("index out of range")
    return self._start + k * self._step

for i in Range(5):
  print(i)