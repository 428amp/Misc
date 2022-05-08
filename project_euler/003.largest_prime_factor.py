from Utilities import is_prime

def main():
  N = 600851475143
  i = 1
  prime_factors = []
  while i <= N**0.5:
    if N/i == N//i:
      N /= i
      prime_factors.append(i)
    i += 1
  prime_factors.append(int(N))
  prime_factors.sort()
  print(prime_factors)
  print(is_prime(prime_factors[-1]), prime_factors[-1])

if __name__ == "__main__":
  main()