import random
import heapq

#copy from 10.1
def mergeSortedArrays(sortedArrays):
  s = []
  minElements = [(sortedArrays[i][0], i, 0) for i in range(len(sortedArrays))]
  heapq.heapify(minElements)
  while len(minElements) > 0:
    cur = heapq.heappop(minElements)
    s.append(cur[0])
    if cur[2]+1 < len(sortedArrays[cur[1]]):
      heapq.heappush(minElements, (sortedArrays[cur[1]][cur[2]+1], cur[1], cur[2]+1))
  return s

def genIncreasingDecreasing(l, k):
  p = [i for i in range(1, l-1)]
  infl = random.sample(p, k-1)
  A = [random.randrange(0, 10)]
  increasing = True
  for i in range(1, l):
    A.append(random.randrange(A[i-1]+1-(increasing^1)*20, A[i-1]-1+increasing*20))
    if i in infl:
      increasing ^= 1
  return A  

def getInflecs(A):
  infl = []
  increasing = True
  for i in range(1, len(A)):
    if (A[i] < A[i-1] and increasing) or (A[i] > A[i-1] and not increasing):
      increasing ^= 1
      infl.append(i)
  return infl

def main():
  for i in range(100):
    L = genIncreasingDecreasing(100, 10)
    # print(L)
    infl = getInflecs(L)+[len(L)]
    sortedArrays = []
    increasing = True
    p = 0
    for i in range(len(infl)):
      if increasing:
        sortedArrays.append(L[p:infl[i]])
      else:
        sortedArrays.append(L[infl[i]-1:p-1:-1])
      increasing ^= 1
      p = infl[i]
    sortedL = mergeSortedArrays(sortedArrays)
    # print(sortedL)
    # print(sorted(L))
    if sortedL != sorted(L):
      print('mismatch')
  else:
    print('no mismatch')
  

if __name__ == '__main__':
  main()