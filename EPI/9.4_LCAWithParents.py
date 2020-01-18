from TreeNode import NodeWithParent as Node
import TreeNode

def getLCA(node1, node2):
  def getDepth(node):
    depth = 0
    if not node.parent:
      return depth
    while node.parent:
      depth += 1
      node = node.parent
    return depth
  depth1 = getDepth(node1)
  depth2 = getDepth(node2)
  if depth1 < depth2:
    for i in range(depth2 - depth1):
      node2 = node2.parent
  elif depth1 > depth2:
    for i in range(depth1 - depth2):
      node1 = node1. parent
  while node1 != node2:
    node1 = node1.parent
    node2 = node2.parent
  return node1

##doesnt work
# def fullTree(depth, parent=None):
#   if depth == 0:
#     return
#   node1 = Node(depth, parent=parent)
#   parent.left = node1
#   node1.left = fullTree(depth-1, node1)
#   node1.right = fullTree(depth-1, node1)

#   node2 = Node(depth, parent=parent)
#   parent.right = node2
#   node2.left = fullTree(depth-1, node2)
#   node2.right = fullTree(depth-1, node2)

depthCt = [0]*10
def fullTree(depth, parent=None):
  if depth == 0:
    return
  depthCt[depth] += 1
  n = Node(str(depth)+'.'+str(depthCt[depth]))
  n.parent = parent
  n.left = fullTree(depth-1, n)
  n.right = fullTree(depth-1, n)
  return n

def fullTreeNoParents(depth):
  if depth == 0:
    return
  return Node(depth, fullTreeNoParents(depth-1), fullTreeNoParents(depth-1))

def main():
  T = fullTree(5)
  TreeNode.traverseBinary(T)
  N = getLCA(T.left.left.left.left, T.left.right.right)
  print(N == T.left)

if __name__ == '__main__':
  main()