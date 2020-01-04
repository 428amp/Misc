import math
class Range:
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
  for j in Range(4):
    print(i, j)

print()
nStep = Range(5, 0, -1.1)
print(nStep._length)
for i in nStep:
  print(i)