def nextPermutation(P):
  for i in reversed(range(len(P))):
    if P[i-1] < P[i]:
      break
  if i == 0:
    return False
  suffixEnd = i-1

  for i in reversed(range(len(P))):
    if P[i] > P[suffixEnd]:
      P[i], P[suffixEnd] = P[suffixEnd], P[i]
      P[suffixEnd+1:] = reversed(P[suffixEnd+1:])
      return True

def prevPermutation(P):
  for i in reversed(range(len(P))):
    if P[i-1] > P[i]:
      break
  if i == 0:
    return False
  suffixEnd = i-1

  for i in reversed(range(len(P))):
    if P[i] < P[suffixEnd]:
      P[i], P[suffixEnd] = P[suffixEnd], P[i]
      P[suffixEnd+1:] = reversed(P[suffixEnd+1:])
      return True

def main():
  P = [i for i in range(4)]
  while True:
    print(P)
    if not nextPermutation(P):
      print('done forward')
      break
  while True:
    print(P)
    if not prevPermutation(P):
      print('done backward')
      break

if __name__ == '__main__':
  main()