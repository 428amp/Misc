def MergeSort(l):
  if len(l) <= 1:
    return l
  left = MergeSort(l[:len(l)//2])
  right = MergeSort(l[len(l)//2:])
  fin = []
  lp = 0
  rp = 0
  for i in range(len(l)):
    if rp == len(right):
      fin.append(left[lp])
      lp += 1
    elif lp == len(left):
      fin.append(right[rp])
      rp += 1
    elif left[lp] < right[rp]:
      fin.append(left[lp])
      lp += 1
    else:
      fin.append(right[rp])
      rp += 1
  return fin

if __name__ == '__main__':
  import random
  sz = random.randrange(10000, 15000)
  l = [i for i in range(sz)]
  b = l[:]
  random.shuffle(l)
  n = MergeSort(l)
  for i in range(sz):
    if b[i] != n[i]:
      print('discrepancy')
      break
  else:
    print('no discrepancy')