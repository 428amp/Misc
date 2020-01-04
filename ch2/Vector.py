class Vector:
  def __init__(self, d):
    self._coords = [0]*d
  
  def __len__(self):
    return len(self._coords)
  
  def __getitem__(self, j):
    return self._coords[j]
  
  def __setitem__(self, j, val):
    self._coords[j] = val

  def __add__(self, other):
    if len(self) != len(other):
      raise ValueError("dimensions must agree")
    result = Vector(len(self))
    for i in range(len(self)):
      result[i] = self[i] + other[i]
    return result
  
  def __eq__(self, other):
    return self._coords == other._coords
  
  def __ne__(self, other):
    return not self == other
  
  def __str__(self):
    return '<' + str(self._coords)[1:-1] + '>'
  
if __name__ == '__main__':
  # testVector = Vector(5)
  # for i in range(5):
  #   testVector[i] = i
  # print(testVector)

  v = Vector(5)
  v[1] = 23
  v[-1] = 45
  print(v)
  print(v[4])
  u = v + v
  print(u)
  total = 0
  for entry in v:
    total += entry
  print(total)