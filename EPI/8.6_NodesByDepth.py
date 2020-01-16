from TreeNode import Node

def NodesByDepth(T):
  if not T:
    return []
  R = []
  currentLayer = [T]
  currentDepth = 0
  while len(currentLayer) != 0:
    currentLayerData = []
    nextLayer = []
    for node in currentLayer:
      currentLayerData.append(node.data)
      if node.left:
        nextLayer.append(node.left)
      if node.right:
        nextLayer.append(node.right)
    R.append(currentLayerData)
    currentDepth += 1
    currentLayer = nextLayer
  return R

def NodesByDepth2(T):
  if not T:
    return []
  R = []
  currentLayer = [T]
  while len(currentLayer) != 0:
    R.append([c.data for c in currentLayer])
    currentLayer = [child for c in currentLayer for child in (c.left, c.right) if child]
  return R

def fullTree(depth):
  if depth == 0:
    return
  return Node(depth, fullTree(depth-1), fullTree(depth-1))

def main(): 
  t = fullTree(5)
  L = NodesByDepth2(t)
  L2 = NodesByDepth(t)
  print(L)
  print(L2)

if __name__ == '__main__':
  main()