from DoublyLinked2 import DoublyLinked2 as DoublyLinkedList

class PermGen:
  def __init__(self, n, p):
    self.L = DoublyLinkedList()

  def __next__(self):
    pass

  def __iter__(self):
    return self

def GenPerm(pool, p):
  if p == 1:
    t = [[i] for i in pool]
    yield from t
    return
  for i in pool:
    yield from [[i]+j for j in GenPerm(pool[:i] + pool[i+1:], p-1)]
    # for k in [[i]+j for j in GenPerm(pool[:i] + pool[i+1:], p-1)]:
    #   yield k

if __name__ == '__main__':
  pool = [i for i in range(5)]
  ct = 0
  for i in GenPerm(pool, 2):
    ct += 1
    print(i)
  print(ct)