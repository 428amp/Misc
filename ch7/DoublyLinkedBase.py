class DoublyLinkedBase:
  class Node:
    __slots__ = 'element', 'prev', 'next'

    def __init__(self, element, prev, next):
      self.element = element
      self.prev = prev
      self.next = next
  
  def __init__(self):
    self.header = self.Node(None, None, None)
    self.trailer = self.Node(None, None, None)
    self.header.next = self.trailer
    self.trailer.prev =self.header
    self.size = 0
  
  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  def insertBetween(self, e, predecessor, successor):
    newest = self.Node(e, predecessor, successor)
    predecessor.next = newest
    successor.prev = newest
    self.size += 1
    return newest
  
  def deleteNode(self, node):
    predecessor = node.prev
    successor = node.next
    predecessor.next = successor
    successor.prev = predecessor
    self.size -= 1
    node.prev = node.next = node.element = none
    return element