from LinkedList import Node
#works unless node being deleted is the last one
def delete(v, L):
  node = L
  while node:
    if node.value == v:
      node.value = node.next.value
      node.next = node.next.next
      return True
    node = node.next
  return False

def main():
  pass

if __name__ == '__main__':
  main()