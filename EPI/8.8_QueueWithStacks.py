class StackQueue:
  def __init__(self):
    self.EQstack = []
    self.DQstack = []

  def enqueue(self, v):
    self.EQstack.append(v)

  def dequeue(self):
    if len(self.DQstack) == 0:
      while len(self.EQstack) > 0:
        self.DQstack.append(self.EQstack.pop())
    if len(self.DQstack) > 0:
      return self.DQstack.pop()
    else:
      return None

def main():
  SQ = StackQueue()
  for i in range(40):
    SQ.enqueue(i)
  for i in range(50):
    print(SQ.dequeue())

if __name__ == '__main__':
  main()