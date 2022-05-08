from cmath import sqrt
from Utilities import is_square

#precomputed square table
squares = [i**2 for i in range(10000)]

def solve_diophantine(D):
  """
  returns minimal x that solves x**2 - Dy**2 = 1
  returns -1 if no x solves
  """
  if is_square(D):
    return -1
  for y in range(1, len(squares)):
    x2 = 1+D*squares[y]
    for x in range(1, len(squares)):
      if squares[x] == x2:
        return x
  return -1

def continued_fraction(n):
  dec = (lambda a: a-a//1)
  C = []
  for i in range(100):
    C.append(n//1)
    r = dec(n)
    if r != 0:
      n = 1/r
    else:
      return
  print(C)

def expand(seq):
  expanded = 0
  for term in reversed(seq):
    expanded = 1/(expanded+term)
  return 1/expanded

def main():
  print(continued_fraction(19**.5))
  print(expand([4,2,1,3,1,2]))
  # max_x = float("-inf")
  # for i in range(101):
  #   x = solve_diophantine(i)
  #   if x > max_x:
  #     max_x = x
  # print(max_x)

if __name__ == "__main__":
  main()