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
def RtoD(R):
  pass

def RtoDSimple(R):
  D = 0
  for char in R:
    D += map[char]
  return D

def main():
  print(RtoDSimple('VVVVV'))

if __name__ == '__main__':
  main()