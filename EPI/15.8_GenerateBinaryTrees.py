from TreeNode import Node

#recursively generate all binary trees with a give node count
#returns list of all trees with given node count
def generateTrees(n):
  if n == 0:
    return [None]
  trees = []
  for i in range(n-1):
    leftTrees = generateTrees(i)
    rightTrees = generateTrees(n-1-i)
    for left in leftTrees:
      for right in rightTrees:
        trees.append(Node(None, left, right))
  return trees
  
def main():
  pass

if __name__ == '__main__':
  main()