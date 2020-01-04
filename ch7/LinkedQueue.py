class LinkedQueue:
  class Node:
    __slots__ = 'element', 'next'

    def __init__(self, element, next):
      self.element = element
      self.next = next
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def __len__(self):
    return self.size
  
  def isEmpty(self):
    return self.size == 0
  
  def first(self):
    if self.isEmpty():
      raise IndexError('Q empty')
    return self.head.element
  
  def dequeue(self):
    if self.isEmpty():
      raise IndexError('Q empty')
    answer = self.head.element
    self.head = self.head.next
    self.size -= 1
    if self.isEmpty():
      self.tail = None
    return answer

  def enqueue(self, e):
    newest = self.Node(e, None)
    if self.isEmpty():
      self.head = newest
    else:
      self.tail.next = newest
    self.tail = newest
    self.size += 1