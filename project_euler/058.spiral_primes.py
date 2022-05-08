from Utilities import is_prime

def main():
  primes_in_diagonal = 0
  diagonal = [1]
  i = 1
  j = 1
  while primes_in_diagonal/len(diagonal) >= .1 or primes_in_diagonal == 0:
  # for j in range(1, 5):
    for k in range(4):
      i += 2*j
      if is_prime(i):
        primes_in_diagonal += 1
      diagonal.append(i)
    j += 1
  print(primes_in_diagonal/len(diagonal))
  print(diagonal[-1])
  print(diagonal[-1]**.5) #len side
  print(len(diagonal))


if __name__ == "__main__":
  main()