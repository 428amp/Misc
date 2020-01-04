import sys

class SudokuPuzzle:
  def __init__(self, filename):
    with open(filename) as f:
      chars = []
      for line in f:
        line = line.replace('\n', '')
        if len(line) != 9:
          raise ValueError('improperly formatted input file')
        for char in line:
          if char not in '123456789.':
            raise ValueError('improperly formatted input file')
          chars.append(char)
    self.gridState = chars
    rows = [[9*i+j for j in range(9)] for i in range(9)]
    columns = [[9*j+i for j in range(9)] for i in range(9)]
    boxes = [[(i//3*27+i%3*3)+j//3*9+j%3 for j in range(9)] for i in range(9)]
    self.groups = {
      'rows':rows,
      'columns':columns,
      'boxes':boxes,
    }
    if not self.validGrid():
      raise ValueError('invalid initial grid')

  def __str__(self):
    # return '\n'.join([''.join(self.gridState[9*i:9*(i+1)]) for i in range(9)])
    s = '\n +---+---+---+\n'
    for i in range(3):
      for j in range(3):
        s += ' |'
        for k in range(3):
          start = 27*i+9*j+k*3
          s += ''.join(self.gridState[start:start+3]) + '|'
        s += '\n'
      s += ' +---+---+---+'+'\n'
    return s

  def indexToRowColBox(self, index):
    '''0 indexed'''
    row, col = index//9, index%9
    for i in range(9):
      curBox = self.groups['boxes'][i]
      if index in curBox:
        box = i
    return (row, col, box)

  def getPossibilities(self, index):
    if self.gridState[index] != '.':
      return []
    row, col, box = self.indexToRowColBox(index)
    myRow = [self.gridState[j] for j in self.groups['rows'][row]]
    myCol = [self.gridState[j] for j in self.groups['columns'][col]]
    myBox = [self.gridState[j] for j in self.groups['boxes'][box]]

    # replace this section with xor
    pool = [str(i) for i in range(1,10)]
    for e in myRow+myCol+myBox:
      if e in pool:
        pool.remove(e)
    return pool

  def checkIfDone(self):
    fin = [str(i) for i in range(1,10)]
    def groupComplete(l):
      group = [self.gridState[i] for i in l]
      if fin != sorted(group):
        return False
      return True
    for group in self.groups['rows']+self.groups['columns']+self.groups['boxes']:
      if not groupComplete(group):
        return False
    return True

  # deprecated, changed to use self.groups
  def OLD_getPossibilities(self, index):
    if self.gridState[index] != '.':
      return []
    r, c = self.indexToRowCol(index)
    column = [self.gridState[9*i+c] for i in range(9)]
    row = self.gridState[9*r:9*r+9]
    btlc = r//3*27+c//3*3
    box = [self.gridState[j] for j in [btlc+i//3*9+i%3 for i in range(9)]]

    pool = [str(i) for i in range(1,10)]
    for i in row+column+box:
      if i in pool:
        pool.remove(i)
    return pool

  # deprecated, changed to use self.groups
  def OLD_checkIfDone(self):
    rcTuples = [(i, i//3+i%3*3) for i in range(9)]
    fin = [str(i) for i in range(1,10)]

    for rc in rcTuples:
      r, c = rc
      column = [self.gridState[9*i+c] for i in range(9)]
      row = self.gridState[9*r:9*r+9]
      btlc = r//3*27+c//3*3
      box = [self.gridState[j] for j in [btlc+i//3*9+i%3 for i in range(9)]]
      row.sort()
      column.sort()
      box.sort()
      if row != fin or column != fin or box != fin:
        return False
    return True

  def validGrid(self):
    def hasDuplicateNumbers(L):
      elements = set()
      for element in L:
        if element in elements:
          return True
        elif element.isnumeric():
          elements.add(element)
      return False
    for key in self.groups:
      group = self.groups[key]
      for g in group:
        nineGroup = [self.gridState[e] for e in g]
        if hasDuplicateNumbers(nineGroup):
          return False
    return True

  def solveWithGuess(self):
    '''return True if solved, False if cannot be solved'''
    while True:
      if '.' not in self.gridState:
        if not self.checkIfDone():
          return False
        return True
      oldGridState = self.gridState[:]
      for i in range(81):
        p = self.getPossibilities(i)
        if len(p) == 1:
          self.gridState[i] = p[0]
      if self.gridState == oldGridState:
        guessSquare = 0
        for i in range(81):
          p = self.getPossibilities(i)
          if len(p) != 0:
            guessSquare = i
            break
        for poss in p:
          prevGridState = self.gridState[:]
          self.gridState[guessSquare] = poss
          self.solveWithGuess()
          if self.checkIfDone():
            return True
          self.gridState = prevGridState
        return False

  # deprecated, attempt to solve without guessing
  def noGuessSolve(self): 
    while True:
      if '.' not in self.gridState:
        if not self.checkIfDone():
          raise ValueError('unsolvable initial puzzle')
        return
      oldGridState = self.gridState[:]
      for i in range(81):
        p = self.getPossibilities(i)
        if len(p) == 1:
          self.gridState[i] = p[0]
          break
      if self.gridState == oldGridState:
        raise ValueError('needs guessing')

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('improper argument count - input as:\nSudokuSolver.py fileName')
    sys.exit()
  fName = sys.argv[1]
  try:
    s = SudokuPuzzle(fName)
    print(s)
    solved = s.solveWithGuess()
  except Exception as e:
    print(e)
    sys.exit()
  print(s, 'solved:', solved)
