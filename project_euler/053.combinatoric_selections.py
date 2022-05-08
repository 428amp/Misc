from Utilities import nCr
import math

"""
for each r in range 1 to 100, find first n s.t. nCr > 1e6
then all N > n w/ N <= 100 NCr > 1e6
"""

def main():
  ct = 0
  for n in range(1, 101):
    for r in range(1, n+1):
      if nCr(n, r) > 10**6:
        ct += 1
  print(ct)

if __name__ == "__main__":
  main()