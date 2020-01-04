def add1(d):
  '''
  takes reversed integer array and adds 1
  '''
  for i in range(len(d)):
    d[i] = (d[i]+1)%10
    if d[i] != 0:
      return
  d.append(1)

def AtoD(d):
  '''
  reversed integer array to int
  '''
  p = 0
  n = 0
  for i in range(len(d)):
    n += d[i]*10**p
    p += 1
  return n

def main():
  for i in range(1000):
    d = [int(c) for c in reversed(str(i))]
    print(AtoD(d))
    add1(d)
    print(AtoD(d))
    print()

if __name__ == '__main__':
  main()