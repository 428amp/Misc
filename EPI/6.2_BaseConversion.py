import math
def convert(n, b1, b2):
  n = [int(n[i]) for i in reversed(range(len(n)))]
  d = 0
  for i in range(len(n)):
    d += n[i]*b1**i
  r = []
  m = math.floor(math.log(d)/math.log(b2))
  while m >= 0:
    newDigit = d//(b2**m)
    d -= b2**m*newDigit
    m -= 1
    r.append(str(newDigit))
  return ''.join(r)+'b'+str(b2)

def main():
  print(convert('1024', 10, 2))

if __name__ == '__main__':
  main()