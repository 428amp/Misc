import heapq

#optimization
def kClosest2(stars, k):
  starHeap = []
  #maxheap while reading stars
  #maxheap by negating all distances
  #if heapsize exceeds k throw away the max
  for star in stars:
    distance = -(star[0]**2+star[1]**2+star[2]**2)**0.5
    heapq.heappush(starHeap, (distance, star))
    if len(starHeap) > k:
      heapq.heappop(starHeap)
  
  kClosest = []
  for i in range(k):
    kClosest.append(heapq.heappop(starHeap))
  # #more useful to return distances instead of stars as different algorithms may return different star sets
  # #comprising the same distance set
  # return [kClosest[i][1] for i in range(k-1, -1, -1)]
  return sorted([-star[0] for star in kClosest])

#where stars is a list of 3 element tuples representing points in 3d space
def kClosest(stars, k):
  starHeap = []
  for star in stars:
    distance = (star[0]**2+star[1]**2+star[2]**2)**0.5
    heapq.heappush(starHeap, (distance, star))
  
  kClosest = []
  for i in range(k):
    kClosest.append(heapq.heappop(starHeap))
  # #more useful to return distances instead of stars as different algorithms may return different star sets
  # #comprising the same distance set
  # return [star[1] for star in kClosest]
  return [star[0] for star in kClosest]

def dumb_kClosest(stars, k):
  def distance(star):
    return (star[0]**2+star[1]**2+star[2]**2)**0.5
  
  starList = []
  for star in stars:
    starList.append((distance(star), star))
  starList.sort()
  return [star[1] for star in starList[:k]]

def main():
  import random
  for i in range(1000):
    stars = []
    for i in range(100):
      stars.append((random.randrange(0,100), random.randrange(0,100), random.randrange(0,100)))
    A = kClosest(stars, 10)
    B = kClosest2(stars, 10)
    # C = dumb_kClosest(stars, 10)
    if not (sorted(A) == sorted(B)):
      print('mismatch')
      print(A)
      print(B)
      print()
    # print(kClosest(stars, 5))
    # print(dumb_kClosest(stars, 5))
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()