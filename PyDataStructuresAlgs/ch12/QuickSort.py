import random

def partition(l, low, high):
  s = low-1
  pivotIndex = random.randrange(low, high)
  pivot = l[pivotIndex]
  l[pivotIndex], l[high] = l[high], l[pivotIndex]
  for i in range(low, high):
    if l[i] <= pivot:
      s += 1
      l[i], l[s] = l[s], l[i]
  l[s+1], l[high] = l[high], l[s+1]
  return s+1

def quickSort(l, low, high):
  if low >= high:
    return
  p = partition(l, low, high)
  quickSort(l, low, p-1)
  quickSort(l, p+1, high)

if __name__ == '__main__':
  import random
  sz = random.randrange(10000, 15000)
  l = [i for i in range(sz)]
  b = l[:]
  random.shuffle(l)
  quickSort(l, 0, len(l)-1)
  for i in range(sz):
    if b[i] != l[i]:
      print('discrepancy')
      break
  else:
    print('no discrepancy')