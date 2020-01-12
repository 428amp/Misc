map = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

#special cases
#IV IX XL XC CD CM
#b2b exceptions not allowed
#only guarantees correct value on properly formatted numerals
def RtoD(R):
  D = 0
  for i in range(len(R) - 1):
    c = R[i]
    d = R[i+1]
    if c == 'I':
      if d == 'V' or d =='X':
        D -= 1
        continue
    elif c == 'X':
      if d == 'L' or d =='C':
        D -= 10
        continue
    if c == 'C':
      if d == 'D' or d =='M':
        D -= 100
        continue
    D += map[c]
  D += map[R[-1]]
  return D

#can use functools.reduce to make code simpler
def RtoD2(R):
  pass

def RtoDSimple(R):
  D = 0
  for char in R:
    D += map[char]
  return D

def main():
  # print(RtoDSimple('VVVVV'))
  print(RtoD('I'))

if __name__ == '__main__':
  main()