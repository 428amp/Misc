from functools import reduce
import math

# def is_prime(n):
#   if n <= 1:
#     return False
#   i = 2
#   while (i <= n**.5):
#     if n%i == 0:
#       return False
#     i += 1
#   return True

def fib(n):
  """
  return nth fib
  """
  preload = [0, 1, 1]
  if n < 3:
    return preload[n]
  f1 = 1
  f2 = 1
  for i in range(n-2):
    t = f2
    f2 = f1 + f2
    f1 = t
  return f2

# def is_prime(n):
#   if n <= 3:
#     return n > 1
#   if n%2 == 0 or n%3 == 0:
#     return False
#   test_1 = 1
#   for i in range(n-1):
#     test_1 = (test_1 * 2) % n
#   if test_1 != 1:
#     return False
#   if fib(n+1)%n != 0:
#     return False
#   return True

def is_prime(n):
  if n <= 3:
    return n > 1
  if n%2 == 0:
    return False
  d = 3
  while d*d <= n:
    if n % d == 0:
      return False
    d += 2
  return True

def is_palindrome(n):
  s_n = str(n)
  return s_n == s_n[::-1]

#probably needs to be changed to a more intelligent alg later
#decide how to deal with special cases
def factorize(n):
  """
  takes n, returns ordered tuple of prime factors that multiply to n
  """
  factorization = []
  R = n
  # for i in range(2, int(n**.5)+1):
  for i in range(2, n+1):
    if (R%i == 0 and is_prime(i)):
      while R%i == 0:
        factorization.append(i)
        R /= i
  return tuple(factorization)

def product(A):
  return reduce(lambda a, b: a*b, A)

def is_square(N):
  return (int(N**.5))**2 == N

def nCr(n, r):
  f = math.factorial
  return f(n) // f(r) // f(n-r)