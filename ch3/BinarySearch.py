def binary_searchM(data, target, low, high):
  if low >= high:
    return False
  mid = (low+high)//2
  n = data[mid]
  if target == n:
    return True
  elif target < n:
    return binary_searchM(data, target, low, mid)
  else:
    return binary_searchM(data, target, mid+1, high)

def binary_search(data, target, low, high):
  pass

if __name__ == '__main__':
  l = [2**n for n in range(10)]
  print(l, '\n')
  c = 0
  for i in range(513):
    if binary_searchM(l, i, 0, 10):
      c += 1
      print(i, '\t', c, 'found so far')
  print('\n', c, 'found in total')