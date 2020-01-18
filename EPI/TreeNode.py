class Node:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

class NodeWithParent:
  def __init__(self, data=None, left=None, right=None, parent=None):
    self.data = data
    self.left = left
    self.right = right
    self.parent = parent

def traverseBinary(node, depth=0):
  if not node:
    return
  traverseBinary(node.left, depth+1)
  # print(node, node.data)
  print(' '*5*depth+str(node.data))
  traverseBinary(node.right, depth+1)
