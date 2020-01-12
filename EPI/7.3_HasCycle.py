from LinkedList import Node

def hasCycle(L):
  if not L:
    return False
  slow = L
  fast = L
  while True:
    if not slow.next:
      return False
    if not (fast.next and fast.next.next):
      return False
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
      return True

def main():
  L1 = Node()
  L1.next = L1
  print(hasCycle(L1))

  L2 = Node()
  print(hasCycle(L2))

  L3 = Node(None, Node(None, Node()))
  print(hasCycle(L3))

  L4 = None
  print(hasCycle(L4))

if __name__ == '__main__':
  main()