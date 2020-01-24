import heapq

#where stars is a list of 3 element tuples representing points in 3d space
def kClosest(stars, k):
  starHeap = []
  for star in stars:
    distance = (star[0]**2+star[1]**2+star[2]**2)**0.5
    heapq.heappush(starHeap, (distance, star))
  
  kClosest = []
  for i in range(k):
    kClosest.append(heapq.heappop(starHeap))
  return [star[1] for star in kClosest]

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
    if kClosest(stars, 10) != dumb_kClosest(stars, 10):
      print('mismatch')
    # print(kClosest(stars, 5))
    # print(dumb_kClosest(stars, 5))
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()