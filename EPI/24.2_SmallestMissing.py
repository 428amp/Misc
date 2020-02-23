#minimum smallest missing for set of len n is n+1
#upper bound for cost is nlogn (sort and run through)
#this alg is max triple runthrough of array so O(n)
def smallestMissing(L):
  i = 0
  ct = 0
  while i < len(L):
    ct += 1
    if 0 < L[i] <= len(L):
      t = L[i] - 1
      L[i], L[t] = L[t], L[i]
      if i == t:
        i += 1
    else:
      i += 1
  for i in range(len(L)):
    if L[i] != i+1:
      return i+1

def main():
  import random
  for i in range(1000):
    sz = random.randrange(10, 100)
    firstMissing = random.randrange(1, sz+2)
    L = [i for i in range(firstMissing)]
    L += random.sample([-(i+1) for i in range(sz)], k=(sz-(firstMissing-1)))
    random.shuffle(L)
    sMissing = smallestMissing(L)
    if sMissing != firstMissing:
      print(L)
      print(firstMissing, sMissing)
      break
  else:
    print('no mismatches')

if __name__ == '__main__':
  main()