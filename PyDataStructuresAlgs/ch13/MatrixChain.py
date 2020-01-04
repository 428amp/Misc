def matrixChain(d):
  '''
  d list of n+1 numbers representing n matrices
  ith matrix has dimensions d[i] x d[i+1]

  N an n x n table where N[i][j] is the minimum cost to multiply from matrix i through j inclusive
  '''
  n = len(d)-1
  N = [[0]*n for i in range(n)]
  for b in range(1, n):
    for i in range(n-b):
      j = i+b
      N[i][j] = min(N[i][k]+N[k+1][j]+d[i]*d[k+1]*d[j+1] for k in range(i, j))
  return N
  
if __name__ == '__main__':
  sz = 15
  d = [i+1 for i in range(sz+1)]
  N = matrixChain(d)
  for i in range(sz):
    for j in range(i+1, sz):
      print('{:>3}{:>3}{:>5}'.format(i, j, N[i][j]))