class CircularQueue:
  class Node:
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
      self.element = element
      self.next = next
  
  def __init__(self):
    self.tail = None
    self.size = 0

  def __len__(self):
    return self.size
  
  def isEmpty(self):
    return self.size = 0
  
  def first(self):
    if self.isEmpty():
      raise ValueError('Q empty')
  head = self.tail.next
  return head.element

  def dequeue(self):
    if self.isEmpty():
      raise ValueError('Q empty')
    oldHead = self.tail.next
    if self.size == 1:
      self.tail = None
    else:
      self.tail.next = oldHead.next
    self.size -= 1
    return oldHead.element
  
  def enqueue(self, e):
    newest = self.Node(e, None)
    if self.isEmpty():
      newest.next = newest
    else:
      newest.next = self.tail.next
    self.tail = newest
    self.size += 1
  
  def rotate(self):
    if self.size > 0:
      self.tail = self.tail.next