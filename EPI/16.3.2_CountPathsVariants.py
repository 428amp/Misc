l = 9
w = 9
A = [[1]*l]+[[1]+[None]*(l-1) for i in range(w-1)]

def countPaths(x, y):
  if A[x][y]:
    return A[x][y]
  A[x][y] = countPaths(x-1, y) + countPaths(x, y-1)
  return A[x][y]

def countMonotone(l):
  return sum([A[i][l-1] for i in range(9)])

def main():
  countPaths(8,8)
  for i in range(1, 10):
    print(countMonotone(i))

if __name__ == '__main__':
  main()