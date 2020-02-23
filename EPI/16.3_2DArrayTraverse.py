l = 5
w = 5
A = [[1]*l]+[[1]+[None]*(l-1) for i in range(w-1)]

#solvable in O(min(x, y)) space by only storing the most recent row/column
#e.g. if you know the values for row 1 you can get row 2 from it and then junk row 1 
#since you only need row 2 to get row 3
def countPaths(x, y):
  if A[x][y]:
    return A[x][y]
  A[x][y] = countPaths(x-1, y) + countPaths(x, y-1)
  return A[x][y]

def main():
  for line in A:
    print(line)
  print(countPaths(l-1, w-1))
  for line in A:
    print(line)

if __name__ == '__main__':
  main()