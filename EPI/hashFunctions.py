import functools

def stringHash(s, modulus):
  MULT = 997
  return functools.reduce(lambda v, c: (v*MULT+ord(c))%modulus, s, 0)

def main():
  pass

if __name__ == '__main__':
  main()


