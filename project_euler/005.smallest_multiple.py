from Utilities import factorize, is_prime, product

def main():
  sub20_primes = []
  for i in range(1, 21):
    if is_prime(i):
      sub20_primes.append(i)
  sol = []
  for prime in sub20_primes:
    P = 1
    while True:
      P *= prime
      if P <= 20:
        sol.append(prime)
      else:
        break
  print(sol)
  print(product(sol))

if __name__ == "__main__":
  main()