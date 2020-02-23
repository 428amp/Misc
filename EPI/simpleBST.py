from TreeNode import Node, traverseBinary

def searchBST(tree, v):
  if not tree:
    return False
  elif tree.data == v:
    return True
  elif tree.data < v:
    return searchBST(tree.right)
  elif tree.data > v:
    return searchBST(tree.left)

def main():
  pass

if __name__ == '__main__':
  main()