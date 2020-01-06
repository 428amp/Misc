def permute(A, P):
  pass

def permuteDumb(A, P):
  newA = [None]*len(P)
  for i in range(len(P)):
    newA[P[i]] = A[i]
  for i in range(len(A)):
    A[i] = newA[i]

def main():
  A = ['a', 'b', 'c', 'd']
  P = [2,0,1,3]
  print(A)
  permuteDumb(A, P)
  print(A)

if __name__ == '__main__':
  main()