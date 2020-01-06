import random
def randomSample(k, A):
  for i in range(k):
    r = random.randint(i, len(A)-1)
    A[i], A[r] = A[r], A[i]

def main():
  A = [i for i in range(10)]
  print(A)
  randomSample(4, A)
  print(A)

if __name__ == '__main__':
  main()