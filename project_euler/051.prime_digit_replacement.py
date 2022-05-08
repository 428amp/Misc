import math

#dumb solution first
#iterate through prime and try all masks

def gen_masked_set(num, mask):
  """
  mask in form 11011
  """
  N = [((num//(10**i))%10) for i in range(math.floor(math.log10(num)), -1, -1)]
  return N

def main():
  print(gen_masked_set(12345, 0))

if __name__ == "__main__":
  main()