def powerSet(S):
  P = []
  l = len(S)
  for i in range(2**l):
    cur = []
    for j in range(l):
      if (i & 1):
        cur.append(S[j])
      i >>= 1
    P.append(cur)
  return P

def main():
  S = [i for i in range(5)]
  print(powerSet(S))

if __name__ == '__main__':
  main()