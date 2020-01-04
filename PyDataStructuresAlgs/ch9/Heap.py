import math

class Heap:
  def __init__(self, data=[]):
    self.data = data
  
  def __len__(self):
    return len(self.data)
  
  def __str__(self):
    sRep = []
    maxDepth = math.ceil(math.log(len(self.data))/math.log(2))
    curDepth = 0
    def isPowerOf2(n):
      return math.ceil(math.log(n)/math.log(2)) == math.floor(math.log(n)/math.log(2))
    for i in range(len(self.data)):
      if isPowerOf2(i+1):
        sRep.append('\n')
        curDepth += 1
      sRep.append('{0:<{width}}'.format(str(self.data[i]), width=2**(2+maxDepth-curDepth)))
    return ''.join(sRep)

  def isEmpty(self):
    return len(self.data) == 0
  
  def swap(self, i, j):
    self.data[i], self.data[j] = self.data[j], self.data[i]

  def push(self, val):
    self.data.append(val)
    cur = len(self.data) - 1
    while self.data[cur] < self.data[(cur-1)//2] and (cur-1)//2 >= 0:
      # print('data[', cur, ']', self.data[cur], 'data[', (cur-1)//2, ']', self.data[(cur-1)//2])
      self.swap(cur, (cur-1)//2)
      cur = (cur-1)//2

  def pop(self):
    self.swap(0, len(self.data)-1)
    val = self.data.pop()
    cur = 0
    while 2*cur+1 < len(self.data):
      left = self.data[2*cur+1]
      small = 2*cur+1
      if 2*cur+2 < len(self.data):
        right = self.data[2*cur+2]
        if right < left:
          small += 1
      if self.data[small] < self.data[cur]:
        self.swap(cur, small)
        cur = small
      else:
        break
    return val

  def min(self):
    return self.data[0]
  
  def heapify(self):
    lastWithChild = (len(self.data)-1)//2
    for cur in range(lastWithChild, -1, -1):
      while 2*cur+1 < len(self.data):
        left = self.data[2*cur+1]
        small = 2*cur+1
        if 2*cur+2 < len(self.data):
          right = self.data[2*cur+2]
          if right < left:
            small += 1
        if self.data[small] < self.data[cur]:
          self.swap(cur, small)
          cur = small
        else:
          break

if __name__ == '__main__':
  import random
  sz = random.randrange(10, 32)
  vals = [i for i in range(sz)]
  print(vals)
  random.shuffle(vals)
  h = Heap(vals)
  h2 = Heap()
  print(vals)
  for i in vals:
    h2.push(i)
  h.heapify()
  print(h)
  popped = []
  popped2 = []
  for i in range(sz):
    popped.append(h.pop())
    popped2.append(h2.pop())
  print(popped)
  print(popped2)
