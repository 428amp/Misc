class CombIterator:
  def __init__(self, n, p):
    self._n = n
    self._p = p
    self._current = list(range(p))
    self._first = True
    
  def __next__(self):
    current = self._current
    p = self._p
    n = self._n

    if self._first:
      self._first = False
      return current
    if p == 0:
      raise StopIteration()
    while not current[0] == n-p:
      for i in range(p-1,-1,-1):
        if current[i] < n-p+i:
          break
      current[i] += 1
      for j in range(i+1, p):
        current[j] = current[j-1] + 1
      return current
    raise StopIteration()

  def __iter__(self):
    return self

def genComb(n, p):
  if p == 0:
    yield []
    return
  current = list(range(p))
  yield current
  while not current[0] == n-p:
    for i in range(p-1,-1,-1):
      if current[i] < n-p+i:
        break
    current[i] += 1
    for j in range(i+1, p):
      current[j] = current[j-1] + 1
    yield current

n = 10
for p in range(11):
  count = 0
  # for c in genComb(n, p):
  for c in CombIterator(n, p):
    count += 1
    if p < 3: 
      print(c)
  print("%dC%d=%d" % (n, p, count))
  print()

# i = CombIterator(10, 0)
# count = 0
# for comb in i:
#   count += 1
#   print(comb)
# print(count)