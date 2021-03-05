def checkWin():
  win1 = [1,1,1,1,1]
  win2 = [2,2,2,2,2]
  hasWin = 0

  #check row win
  for row in range(gridSize):
    for i in range(gridSize-4):
      chunk = board[row][i:i+5]
      if chunk == win1:
        return 1
      elif chunk == win2:
        return 2
  
  #check col win
  for col in range(gridSize):
    for i in range(gridSize-4):
      if board[i][col] == 0:
        continue
      chunk = [board[i+j][col] for j in range(5)]
      if chunk == win1:
        return 1
      elif chunk == win2:
        return 2

  #check downDiag win
  for col in range(gridSize-4):
    for i in range(gridSize-4):
      chunk = [board[i+j][col+j] for j in range(5)]
      if chunk == win1:
        return 1
      elif chunk == win2:
        return 2
  
  #check upDiag win
  for col in range(gridSize-4):
    for i in range(gridSize-4):
      chunk = [board[i+4-j][col+j] for j in range(5)]
      if chunk == win1:
        return 1
      elif chunk == win2:
        return 2
  
  #nowin return -1
  return hasWin

  #clean code duplication
#deal with chains that are technically "open" but can't be finished to len5 due to board edges
def checkChain(length, color):
  """
  find # of chains of specified length and color. broken down into capped on 0,1 ends
  length can be 2-4 (directional checks are messed up by len1 chains)
  """
  match = [color for i in range(length)]
  cap0, cap1 = 0, 0

  #check row -
  for row in range(gridSize):
    for startCol in range(gridSize-length+1):
      chunk = board[row][startCol:startCol+length]
      if chunk == match:
        #check ends
        if startCol == 0:
          capLeft = not color
        else:
          capLeft = board[row][startCol-1]
        if startCol == gridSize-length:
          capRight = not color
        else:
          capRight = board[row][startCol+length]
        if color not in [capLeft, capRight]: #throw out longer chains
          if capLeft == -1 and capRight == -1:
            cap0 += 1
          elif (capLeft == -1 and capRight == (not color)) or (capLeft == (not color) and capRight == -1):
            cap1 += 1

  #check column |
  for col in range(gridSize):
    for startRow in range(gridSize-length+1):
      chunk = [board[startRow+i][col] for i in range(length)]
      if chunk == match:
        if startRow == 0:
          capTop = not color
        else:
          capTop = board[startRow-1][col]
        if startRow == gridSize-length:
          capBot = not color
        else:
          capBot = board[startRow+length][col]
        if color not in [capTop, capBot]:
          if capTop == -1 and capBot == -1:
            cap0 += 1
          elif (capTop == -1 and capBot == (not color)) or (capTop == (not color) and capBot == -1):
            cap1 += 1

  #check diagDown \
  for col in range(gridSize-length+1):
    for row in range(gridSize-length+1):
      chunk = [board[row+i][col+i] for i in range(length)]
      if chunk == match:
        if row == 0 or col == 0:
          capLeft = not color
        else:
          capLeft = board[row-1][col-1]
        if col == gridSize-length or row == gridSize-length:
          capRight = not color
        else:
          capRight = board[row+length][col+length]
        if color not in [capLeft, capRight]:
          if capLeft == -1 and capRight == -1:
            cap0 += 1
          elif (capLeft == -1 and capRight == (not color)) or (capLeft == (not color) and capRight == -1):
            cap1 += 1

  #check diagUp /
  for col in range(gridSize-length+1):
    for row in range(length-1, gridSize):
      chunk = [board[row-i][col+i] for i in range(length)]
      if chunk == match:
        if row == gridSize-1 or col == 0:
          capLeft = not color
        else:
          capLeft = board[row+1][col-1]
        if col == gridSize-length or row == length-1:
          capRight = not color
        else:
          capRight = board[row-length][col+length]
        if color not in [capLeft, capRight]:
          if capLeft == -1 and capRight == -1:
            cap0 += 1
          elif (capLeft == -1 and capRight == (not color)) or (capLeft == (not color) and capRight == -1):
            cap1 += 1

  return cap0, cap1