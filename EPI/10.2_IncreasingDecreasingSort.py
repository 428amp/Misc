import random
def genIncreasingDecreasing(l, k):
  p = [i for i in range(1, l-1)]
  infl = random.sample(p, k-1)
  A = [random.randrange(0, 10)]
  increasing = True
  for i in range(1, l):
    A.append(random.randrange(A[i-1]-(increasing^1)*20, A[i-1]+increasing*20))
    if i in infl:
      increasing ^= 1
  return A  

def main():
  L = genIncreasingDecreasing(20, 1)
  print(L)

if __name__ == '__main__':
  main()