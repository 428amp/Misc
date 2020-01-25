import heapq

def dumbMergeSortedArrays(sortedArrays):
  s = []
  for a in sortedArrays:
    s += a
  s.sort()
  return s

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

def main():
  import random
  P = [i for i in range(100)]
  for i in range(100):
    sortedArrays = []
    for i in range(random.randrange(5, 10)):
      currentArray = random.sample(P, random.randrange(5,10))
      currentArray.sort()
      sortedArrays.append(currentArray)
    dumbMerged = dumbMergeSortedArrays(sortedArrays)
    merged = mergeSortedArrays(sortedArrays)
    if dumbMerged != merged:
      print('mismatch')
      break
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()