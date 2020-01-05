import math
def enumPrimesDumb(n):
  primes = []
  for i in range(2, n+1):
    prime = True
    for j in range(2,i-1):
      if i%j == 0:
        prime = False
        break
    if prime:
      primes.append(i)
  return primes

def enumPrimes2(n):
  primes = []
  for i in range(2, n+1):
    prime = True
    for p in primes:
      if p > math.sqrt(i):
        break
      if i%p == 0:
        prime = False
        break
    if prime:
      primes.append(i)
  return primes

def enumPrimes3(n):
  isPrime = [False]*2+[True]*(n-1)
  for i in range(2, n+1):
    if not isPrime[i]:
      continue
    for j in range(2*i, n+1, i):
      isPrime[j] = False
  return [i for i in range(len(isPrime)) if isPrime[i]]


def main():
  # print(enumPrimes3(7))
  for i in range(1000):
    if enumPrimes3(i) != enumPrimes2(i):
      print('disagree')
  else:
    print('agree')

if __name__ == '__main__':
  main()