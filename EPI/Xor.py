def rightPropagate(n):
  pass

def xMultipleOf2PowerN(x, n):
  return (x & 2**n-1) is 0

def testIfPowerOf2(n):
  # says 0 is power of 2 due to 0&-1 behavior
  return (n) & (n-1) is 0

def main():
  for i in range(33):
    if testIfPowerOf2(i):
      print('{:<2} is a power of 2'.format(i))

  for i in range(2,5):
    for j in range(33):
      if xMultipleOf2PowerN(j, i):
        print('{:<2} is a multiple of {:<2}'.format(j, int(2**i)))

if __name__ == '__main__':
  main()