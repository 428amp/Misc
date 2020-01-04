def LCS(X, Y):
  '''
  find length of longest common substring of strings X, Y
  returns table L s.t. L[j][k] is length of LCS for X[0:j], Y[0:k]
  '''
  n, m = len(X), len(Y)
  L = [[0]*(m+1) for i in range(n+1)]

  for j in range(n):
    for k in range(m):
      if X[j] == Y[k]:
        L[j+1][k+1] = L[j][k]+1
      else:
        L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
  return L

def LCSSolution(X, Y, L):
  '''
  find longest common substring of strings X, Y
  returns string
  '''
  solution = []
  j, k = len(X), len(Y)
  while L[j][k] > 0 and j >= 0 and k >= 0:
    # print(j, X[j-1], '|', k, Y[k-1])
    if X[j-1] == Y[k-1]:
      solution.append(X[j-1])
      j -= 1
      k -= 1
    elif L[j-1][k] >= L[j][k-1]:
      j -= 1
    else:
      k -= 1
  return ''.join(reversed(solution))

def main():
  import random
  sz = 50
  text1 = ''
  text2 = ''
  for i in range(sz):
    text1 += str(random.randrange(0,5))
    text2 += str(random.randrange(5,10))
  testCt = 100
  letters = 'abcdefghijklmnopqrstuvwxyz'
  LCStest = ''
  for i in range(10):
    LCStest += letters[random.randrange(0,26)]
  curIndex = 0
  for letter in LCStest:
    nextIndex = random.randrange(curIndex+1, len(text1)-1)
    text1 = text1[:nextIndex]+letter+text1[nextIndex:]
    curIndex = nextIndex
  curIndex = 0
  for letter in LCStest:
    nextIndex = random.randrange(curIndex+1, len(text2)-1)
    text2 = text2[:nextIndex]+letter+text2[nextIndex:]
    curIndex = nextIndex
  print('e:', LCStest)
  L = LCS(text1, text2)
  # for line in L:
  #   print(line)
  print('s:', LCSSolution(text1, text2, L))

if __name__ == '__main__':
  main()
