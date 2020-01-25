import heapq

def median(stream):
  leftHeap = [] #maxheap left
  rightHeap = [] #minheap right
  first = True
  for num in stream:
    if first:
      heapq.heappush(leftHeap, num)
      first = False
      continue

    if num > -leftHeap[0]:
      heapq.heappush(rightHeap, num)
    else:
      heapq.heappush(leftHeap, -num)

    while len(leftHeap) < len(rightHeap):
      heapq.heappush(leftHeap, -heapq.heappop(rightHeap))
  if len(stream)%2 != 0:
    return -heapq.heappop(leftHeap)
  else:
    return (-heapq.heappop(leftHeap)+heapq.heappop(rightHeap))/2

def dumb_median(stream):
  stream.sort()
  if len(stream)%2 != 0:
    return stream[len(stream)//2]
  else:
    return sum(stream[len(stream)//2-1:len(stream)//2+1])/2

def main():
  import random
  P = [i for i in  range(100)]
  for i in range(1000):
    stream = random.choices(P, k=random.randrange(10, 50))
    med = median(stream)
    dumb_med = dumb_median(stream)
    if med != dumb_med:
      print('mismatch')
      print(med)
      print(dumb_med)
      break
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()