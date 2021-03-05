import random
import numpy as np

gridSize = 9
board = np.full((gridSize, gridSize), -1)
turn = 0
piecePool = ["X", "O", "-"]
pieceMap = {"X":0, "O":1, "-":-1}
BLACK = 0
WHITE = 1

def drawBoard():
  hSpace = "   "
  vSpace = "\n"
  print("\n ", end=hSpace)
  for i in range(gridSize):
    print(i%10, end=hSpace)
  print(vSpace)
  
  for i in range(gridSize):
    row = board[i]
    print(i%10, end=hSpace)
    for cell in row:
      print(piecePool[cell], end=hSpace)
    print(vSpace)

def chainToA(chain):
  A = np.empty(len(chain))
  for i in range(len(chain)):
    A[i] = pieceMap[chain[i]]
  return A

def AtoChain(A):
  chain = ""
  for l in A:
    chain += piecePool[l]
  return chain

#countChain ver using numpy commands
def countChainNp(chain):
  match = chain
  length = len(chain)
  ct = 0

  #check row -
  for row in range(gridSize):
    for startCol in range(gridSize-length+1):
      chunk = board[row, startCol:startCol+length]
      if np.array_equal(chunk, match):
        ct += 1
  
  #check column |
  for col in range(gridSize):
    for startRow in range(gridSize-length+1):
      chunk = board[startRow:startRow+length, col]
      if np.array_equal(chunk, match):
        ct += 1
  
  #check diagDown \
  for i in range(-gridSize+1, gridSize):
    diag = board.diagonal(i)
    diagLen = len(diag)
    if diagLen < length:
      continue
    for j in range(diagLen-length+1):
      chunk = diag[j:j+length]
      if np.array_equal(chunk, match):
        ct += 1

  #check diagUp /
  flipBoard = np.fliplr(board)
  match = np.flip(match)
  for i in range(-gridSize+1, gridSize):
    diag = flipBoard.diagonal(i)
    diagLen = len(diag)
    if diagLen < length:
      continue
    for j in range(diagLen-length+1):
      chunk = diag[j:j+length]
      if np.array_equal(chunk, match):
        ct += 1

  return ct

#new ver countChain of checkChain more general (takes any chains)
#calling pattern is different from old checkChain
#function executes too slowly
def countChain(chain):
  match = chain
  length = len(chain)
  ct = 0

  #check row -
  for row in range(gridSize):
    for startCol in range(gridSize-length+1):
      chunk = board[row][startCol:startCol+length]
      if np.array_equal(chunk, match):
        ct += 1

  #check column |
  for col in range(gridSize):
    for startRow in range(gridSize-length+1):
      chunk = [board[startRow+i][col] for i in range(length)]
      if np.array_equal(chunk, match):
        ct += 1

  #check diagDown \
  for col in range(gridSize-length+1):
    for row in range(gridSize-length+1):
      chunk = [board[row+i][col+i] for i in range(length)]
      if np.array_equal(chunk, match):
        ct += 1

  #check diagUp /
  for col in range(gridSize-length+1):
    for row in range(length-1, gridSize):
      chunk = [board[row-i][col+i] for i in range(length)]
      if np.array_equal(chunk, match):
        ct += 1
  
  return ct

def count2s(color):
  c1 = [color for i in range(2)]+[-1]
  c2 = [-1]+[color for i in range(2)]
  c3 = [-1]+[color for i in range(2)]+[-1]
  c4 = [color for i in range(3)]+[-1]
  c5 = [-1]+[color for i in range(3)]

  return countChain(c1)+countChain(c2)-(countChain(c3)+countChain(c4)+countChain(c5))

usefulChains = [
  "XX-",
]
def getScore(color):
  # ct = 0
  # for chain in usefulChains:
  #   ct += countChainNp(chainToA(chain))
  # return ct

  c11 = countChainNp([color for i in range(2)]+[-1])
  c12 = countChainNp([-1]+[color])
  c13 = countChainNp([-1]+[color]+[-1])
  c14 = countChainNp([color for i in range(2)]+[-1])
  c15 = countChainNp([-1]+[color for i in range(2)])
  e01 = c13
  e11 = c11 + c12 - (c14 + c15) - 2*c13

  c21 = countChainNp([color for i in range(2)]+[-1])
  c22 = countChainNp([-1]+[color for i in range(2)])
  c23 = countChainNp([-1]+[color for i in range(2)]+[-1])
  c24 = countChainNp([color for i in range(3)]+[-1])
  c25 = countChainNp([-1]+[color for i in range(3)])
  e02 = c23
  e12 = c21 + c22 - (c24 + c25) - 2*c23

  c31 = countChainNp([color for i in range(3)]+[-1])
  c32 = countChainNp([-1]+[color for i in range(3)])
  c33 = countChainNp([-1]+[color for i in range(3)]+[-1])
  c34 = countChainNp([color for i in range(4)]+[-1])
  c35 = countChainNp([-1]+[color for i in range(4)])
  e03 = c33
  e13 = c31 + c32 - (c34 + c35) - 2*c33

  c41 = countChainNp([color for i in range(4)]+[-1])
  c42 = countChainNp([-1]+[color for i in range(4)])
  c43 = countChainNp([-1]+[color for i in range(4)]+[-1])
  c44 = countChainNp([color for i in range(5)]+[-1])
  c45 = countChainNp([-1]+[color for i in range(5)])
  e04 = c43
  e14 = c41 + c42 - (c44 + c45) - 2*c43

  ea5 = countChainNp([color for i in range(5)])

  score = .00*e11 + .1*e01 + e12 + 3*e02 + 4*e13 + 64*e03 + 32*e14 + 1024*e04 + 65536*ea5
  return score

def miniMax(depth, maximizingPlayer, alpha, beta):
  pruned = False
  if depth == 0:
    return getScore(turn)-getScore(not turn), None
  if maximizingPlayer:
    maxScore = -float("inf")
    for row in range(gridSize):
      for col in range(gridSize):
        if board[row][col] == -1:
          board[row][col] = turn
          score = miniMax(depth-1, False, alpha, beta)[0]
          board[row][col] = -1
          if score > maxScore:
            maxScore = score
            maxScoreLoc = (row, col)
          alpha = max(alpha, maxScore)
          if score >= beta:
            # print("pruned")
            pruned = True
            break        
      if pruned:
        break  
    return maxScore, maxScoreLoc
  else:
    minScore = +float("inf")
    for row in range(gridSize):
      for col in range(gridSize):
        if board[row][col] == -1:
          board[row][col] = (not turn)
          score = miniMax(depth-1, True, alpha, beta)[0]
          board[row][col] = -1
          if score < minScore:
            minScore = score
            minScoreLoc = (row, col)
          beta = min(beta, minScore)
          if score <= alpha:
            # print("pruned")
            pruned = True
            break
      if pruned:
        break
    return minScore, minScoreLoc

def hasWin():
  return countChainNp(chainToA("XXXXX")) + countChainNp(chainToA("OOOOO")) > 0

def moveRandomly(color):
  while True:
    row = random.randrange(0, gridSize)
    col = random.randrange(0, gridSize)
    if board[row][col] == -1:
      board[row][col] = color
      return

def dumbMove(color):
  maxScore = -float("inf")
  bestPoint = None
  for row in range(gridSize):
    for col in range(gridSize):
      if board[row][col] == -1:
        board[row][col] = color
        curScore = getScore(color) - getScore(not color)
        if curScore > maxScore:
          maxScore = curScore
          bestPoint = (row, col)
        board[row][col] = -1
  board[bestPoint[0]][bestPoint[1]] = color

def main():
  global turn
  drawBoard()

  # board[gridSize//2][gridSize//2] = turn
  # turn = not turn
  # for i in range(gridSize**2//2):
  #   dumbMove(turn)
  #   # moveRandomly(turn)
  #   turn = not turn
  #   drawBoard()
  #   if hasWin():
  #     print("has win")
  #     break
  
  # for i in range(gridSize**2//2):
  while not hasWin():
    bestLoc = miniMax(1, True, float("inf"), float("-inf"))[1]
    board[bestLoc[0]][bestLoc[1]] = turn
    turn = not turn
    drawBoard()
    if hasWin():
      print("has win")
      break

  # for i in range(5):
  #   board[0][i] = 0
  # drawBoard()
  # print(hasWin())

  # drawBoard()
  # print(getScore(0))
  # print(miniMax(2, True))

  # for i in range(gridSize**2//2):
  #   moveRandomly(turn)
  #   turn = not turn
  # drawBoard()
  # print(countChainNp(chainToA("XX-")))

  # drawBoard()
  # chainL = 2
  # playerX = checkChain(chainL, 0)
  # playerO = checkChain(chainL, 1)
  # print("X has {}cap0 and {}cap1 len{} chains".format(playerX[0], playerX[1], chainL))
  # print("O has {}cap0 and {}cap1 len{} chains".format(playerO[0], playerO[1], chainL))

if __name__ == '__main__':
  main()