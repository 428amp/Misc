import ctypes

class DynamicArray:
  def __init__(self):
    self._n = 0
    self._capacity = 1
    self._A = self._make_array(self._capacity)

  def __len__(self):
    return self._n
  
  def __getitem__(self, k):
    if not 0 <= k < self._n:
      raise IndexError('invalid index')
    return self._A[k]
  
  def __str__(self):
    s = '[' + ', '.join([str(a) for a in self._A[0:self._n]]) + ']'
    return s

  def append(self, obj):
    if self._n == self._capacity:
      self._resize(2*self._capacity)
    self._A[self._n] = obj
    self._n += 1
  
  def insert(self, k, value):
    if self._n == self._capacity:
      self._resize(2*self._capacity)
    for j in range(self._n, k, -1):
      self._A[j] = self._A[j-1]
    self._A[k] = value
    self._n += 1
  
  def remove(self, value):
    for k in range(self._n):
      if self._A[k] == value:
        for j in range(k, self._n-1):
          self._A[j] = self._A[j+1]
        self._A[self._n-1] = None
        self._n -= 1
        return
    raise ValueError('value not found')
  
  def _resize(self, c):
    B = self._make_array(c)
    for k in range(self._n):
      B[k] = self._A[k]
    self._A = B
    self._capacity = c
  
  def _make_array(self, c):
    return (c*ctypes.py_object)()

if __name__ == '__main__':
  import random
  a = DynamicArray()
  l = [i for i in range(35)]
  for i in l:
    a.append(i)
  for i in range(len(l)):
    if a[i] != l[i]:
      print('list discrepancy')
  else:
    print('no list discrepancies\n')

  b = DynamicArray()
  print(b)
  for i in range(100):
    b.insert(random.randrange(0, len(b)+1), i)
  print(b)
  for i in range(100):
    b.remove(i)
  print(b)
