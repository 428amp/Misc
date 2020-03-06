#if odd # negative exclude largest  negative#
#if even# negative exclude smallest positive#
#if has 0s and negCt even exclude 0 (does not matter 1 or 2+ 0s)
#if has 0s and negCt odd exclude non 0 (does not matter what)
def maxProductExcludeOne(L):
  largestNegativeSoFar = -1
  smallestPositiveSoFar = -1
  negCt = 0
  has0s = -1
  for i in range(len(L)):
    if L[i] == 0:
      has0s = i 
    elif L[i] < 0:
      negCt += 1
      if largestNegativeSoFar == -1:
        largestNegativeSoFar = i
      if L[i] > L[largestNegativeSoFar]:
        largestNegativeSoFar = i 
    elif L[i] > 0:
      if smallestPositiveSoFar == -1:
        smallestPositiveSoFar = i
      if L[i] < L[smallestPositiveSoFar]:
        smallestPositiveSoFar = i
  if negCt%2 == 0:
    if has0s != -1:
      excluded = has0s
    else:
      excluded = smallestPositiveSoFar
  else:
    excluded = largestNegativeSoFar
  product = 1
  for i in range(len(L)):
    if i != excluded:
      product *= L[i]
  return product

def dumb_maxProductExcludeOne(L):
  maxProd = None
  for i in range(len(L)):
    cur = 1
    for j in range(len(L)):
      if j != i:
        cur *= L[j]
    if not maxProd:
      maxProd = cur
      continue
    if cur > maxProd:
      maxProd = cur
  return maxProd

def main():
  #cases of interest
  L = [None]*6
  L[0] = [3, 2, -1, 4]
  L[1] = [0, 0, -1, -2, 3, 4, 5]
  L[2] = [0, -1, -2, 3, 4, 5]
  L[3] = [0, 0, -1, 2, 3, 4, 5]
  L[4] = [0, -1, 2, 3, 4, 5]
  L[5] = [-1, -2, 3, 4, 5]
  for l in L:
    print(maxProductExcludeOne(l), dumb_maxProductExcludeOne(l))

if __name__ == '__main__':
  main()