from operator import is_
from Utilities import is_prime, fib

def main():
  prime_sum = 0
  for i in range(2*10**6):
    if is_prime(i):
      prime_sum += i
  print(prime_sum)

if __name__ == "__main__":
  main()