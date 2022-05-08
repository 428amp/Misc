import Utilities

def sum_squares(n):
  """
  sum squares of natural nums from 1 to n
  """
  S = 0
  for i in range(1, n+1):
    S += i**2
  return S

def squares_sum(n):
  """
  square sum of natural nums from 1 to n
  """
  S = sum([i for i in range(1, n+1)])
  return S**2

def main():
  print(abs(sum_squares(100) - squares_sum(100)))

if __name__ == "__main__":
  main()