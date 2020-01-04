def steppingGame(A):
  farthest = 0
  for i in range(len(A)):
    farthest = max(A[i]+i, farthest)
    print(i, farthest)
    if farthest >= len(A)-1:
      return True
  return False

def main():
  print(steppingGame([1,2,0,1]))

if __name__ == '__main__':
  main()