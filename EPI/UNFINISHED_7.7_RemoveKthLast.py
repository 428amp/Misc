#traverse k nodes, then start another parallel traversal from the front
def removeKthLast(L, k):
  first = L
  for i in range(k):
    first = first.next
  kth = L
  while first:
    first = first.next
    kth = kth.next
  return kth

def main():
  pass

if __name__ == '__main__':
  main()