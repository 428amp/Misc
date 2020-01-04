def prefix_average1(S):
  n = len(S)
  A = [0] * n
  for i in range(n):
    total = 0
    for j in range(i+1):
      total += S[j]
    A[i] = total/(i+1)
  return A

def prefix_average2(S):
  n = len(S)
  A = [0] * n
  for i in range(n):
    A[i] = sum(S[0:i+1])/(i+1)
  return A

def prefix_average3(S):
  n = len(S)
  A = [0] * n
  total = 0
  for i in range(n):
    total += S[i]
    A[i] = total/(i+1)
  return A

if __name__ == '__main__':
  l = [i for i in range(10)]
  p1 = prefix_average1(l)
  p2 = prefix_average2(l)
  p3 = prefix_average3(l)

  print(p1)
  print(p2)
  print(p3)
  if p1 == p2 and p2 == p3:
    print('equal')
  else:
    print('not equal')
