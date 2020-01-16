class CircularQueue:
  def __init__(self, capacity=10):
    self.Q = [None]*capacity
    self.capacity = capacity
    self.head = 0
    self.size = 0
  
  def isEmpty(self):
    return self.size == 0
  
  def enqueue(self, v):
    if self.size == self.capacity - 1:
      self.resize(self.capacity*2)
    self.Q[(self.head+self.size)%self.capacity] = v
    self.size += 1

  def dequeue(self):
    if self.isEmpty():
      return
    r = self.Q[self.head]
    self.Q[self.head] = None
    self.head = (self.head+1)%self.capacity
    self.size -= 1
    return r

  def resize(self, newCapacity):
    newQ = [None]*newCapacity
    for i in range(self.capacity-1):
      newQ[i] = self.Q[(self.head+i)%self.capacity]
    self.Q = newQ
    self.head = 0
    self.capacity = newCapacity

def main():
  Q = CircularQueue()
  for i in range(40):
    Q.enqueue(i)
  for i in range(40):
    print(Q.dequeue())
  for i in range(20):
    Q.enqueue(i)
  for i in range(30):
    print(Q.dequeue())
if __name__ == '__main__':
  main()