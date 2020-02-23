def gcd(a, b):
  larger = a
  smaller = b
  if larger < smaller:
    larger, smaller = smaller, larger
  
  while True:
    diff = larger - smaller
    # print(diff)
    if diff == 0:
      return smaller
    else:
      larger, smaller = smaller, diff
      if larger < smaller:
        larger, smaller = smaller, larger

def gcd2(a, b):
  #ensure a > b
  if a < b:
    a, b = b, a
  while True:
    r = a - b
    while r > b:
      r -= b
    if r == 0:
      return b
    a = b
    b = r

def main():
  import math
  import random
  for i in range(10000):
    a = random.randrange(1, 10000)
    b = random.randrange(1, 10000)
    # print(a, b)
    # print(math.gcd(a, b), gcd(a, b))
    if math.gcd(a, b) != gcd2(a, b):
      print(math.gcd(a, b))
      print(gcd2(a, b))
      break
  else:
    print('no mismatches')

if __name__ == '__main__':
  main()