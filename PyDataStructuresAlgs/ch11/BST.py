class Node:
  def __init__(self, value, parent=None, left=None, right=None):
    self.value = value
    self.parent = parent
    self.left = left
    self.right = right

# insert key and return new root
def insert(node, value):
  if not node:
    return Node(value)
  if node.value < value:
    if node.right:
      insert(node.right, value)
    else:
      node.right = Node(value, node)
  else:
    if node.left:
      insert(node.left, value)
    else:
      node.left = Node(value, node)
  return node

# delete key and return new root
def deleteKey(node, value):
  if node is None:
    return None
  if node.value < value:
    node.right = deleteKey(node.right, value)
  elif node.value > value:
    node.left = deleteKey(node.left, value)
  elif node.value == value:
    # no or 1 child
    if node.left == None:
      right = node.right
      node = None
      return right
    elif node.right == None:
      left = node.left
      node = None
      return left
    # 2 children
    # get maxval from left tree
    cur = node.left
    while cur.right:
      cur = cur.right
    node.value = cur.value
    node.left = deleteKey(node, value)

def traverse(node):
  if node == None:
    return
  else:
    traverse(node.left)
    print(node.value)
    traverse(node.right)

def search(node, value):
  if node.value == value:
    return True
  elif node.value <= value:
    return search(node.right, value)
  elif node.value > value:
    return search(node.left, value)
  elif node == None:
    return False

if __name__ == '__main__':
  import random
  import math
  sz = random.randrange(0, 50)
  l = [i for i in range(sz)]
  random.shuffle(l)
  r = None
  for i in l:
    r = insert(r, i)
  print('populated tree traverse | sz =', sz)
  traverse(r)
  print()
  for i in range(sz+100):
    r = deleteKey(r, i)
  print('deleted tree traverse')
  traverse(r)
  print()
  # for i in range(sz):
  #   print('{0:<{width1}} {1}'.format(i, search(r, i), width1=math.ceil(math.log(sz))))
  