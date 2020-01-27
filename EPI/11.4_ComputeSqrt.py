#get largest int k s.t. k**2 < n
#binary search type logic
def sqrtFloor(n):
  l = 0
  r = n
  while l <= r:
    m = (l+r)//2
    if m**2 < n:
      l = m+1
    elif m**2 > n:
      r = m-1
    elif m**2 == n:
      return m
  return l-1

def dumb_sqrtFloor(n):
  k = 0
  while True:
    if (k+1)**2 > n:
      return k
    k += 1

import math
def dumber_sqrtFloor(n):
  return int(math.floor(math.sqrt(n)))

def main():
  for i in range(1000):
    A = sqrtFloor(i)
    # B = dumb_sqrtFloor(i)
    C = dumber_sqrtFloor(i)
    if A != C:
      print('mismatch')
      print('i:', i)
      print(A)
      print(C)
      break
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()