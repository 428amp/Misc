from DoublyLinkedBase import DoublyLinkedBase

class DoublyLinked2(DoublyLinkedBase):
  def __init__(self):
    super().__init__()
  
  def __str__(self):
    selfStr = ''
    cur = self.header
    while cur.next is not None:
      cur = cur.next
      selfStr += cur.element
    return selfStr

  def push(self, e):
    self.insertBetween(e, self.header, self.header.next)

if __name__ == '__main__':
  l = DoublyLinked2()
  print(len(l))
  print(l)