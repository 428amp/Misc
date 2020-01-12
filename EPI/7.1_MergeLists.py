from LinkedList import Node

#merge 2 sorted lists (arrays) with O(1) space complexity
#assume the first list has enough space to hold both once merged
def mergeLists2(L1, L2):
  #move L1 to end of L1 then merge as you would with a separate temp array
  pass

def mergeListsDumb(L1, L2):
  combined = []

#merge 2 sorted linked lists with O(1) space complexity
def mergeLists(L1, L2):
  dummyHead = tail = Node()
  while L1 and L2:
    if L1.data < L2.data:
      tail.next = L1
      L1 = L1.next
    else:
      tail.next = L2
      L2 = L2.next
    tail = tail.next
  if L1:
    tail.next = L1
  else:
    tail.next = L2
  return dummyHead.next

def main():
  import random
  L1 = []
  L2 = []
  for i in range(10):
    L1.append(random.randrange(0, 50))
    L2.append(random.randrange(0, 50))
  L1.sort()
  L1.reverse()
  L2.sort()
  L2.reverse()
  prev = None
  for v in L1:
    newNode = Node(v, prev)
    prev = newNode
  Ln1 = newNode
  prev = None
  for v in L2:
    newNode = Node(v, prev)
    prev = newNode
  Ln2 = newNode

  LnM = mergeLists(Ln1, Ln2)
  L = []
  while LnM:
    L.append(LnM.data)
    LnM = LnM.next
  print(L == sorted(L1 + L2))
  print(len(L))

  # L1c = []
  # while cur.next != None:
  #   L1c.append(cur.data)
  #   cur = cur.next
  # L1c.append(cur.data)
  # print(list(reversed(L1)) == L1c)

if __name__ == '__main__':
  main()