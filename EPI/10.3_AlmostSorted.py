import random
import heapq

#doesn't create randomly almost-sorted array but result is guaranteed to be k-almost-sorted
def genAlmostSorted(l, k):
  L = [i for i in range(l)]
  i = 0
  while i < l-k:
    L[i:i+k] = random.sample(L[i:i+k], k)
    i += k
  L[i:i+k] = random.sample(L[i:], len(L)-i)
  return L  

#all elements in A are within k of their correct location
def sortAlmostSorted(A, k):
  s = []
  h = A[:k]
  heapq.heapify(h)
  i = k
  while i < len(A):
    s.append(heapq.heappop(h))
    heapq.heappush(h, A[i])
    i += 1
  for i in range(k):
    s.append(heapq.heappop(h))
  return s

def main():
  for i in range(1000):
    l = random.randrange(50, 100)
    k = random.randrange(1, 10)
    almostSorted = genAlmostSorted(l, k)
    dumbSorted = sorted(almostSorted)
    kSorted = sortAlmostSorted(almostSorted, k)
    if dumbSorted != kSorted:
      print('mismatch')
      break
    # print(almostSorted)
    # print(sortAlmostSorted(almostSorted, 4))
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()