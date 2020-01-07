def getColumnNum(colID):
  columnNum = 0
  power = 0
  for C in reversed(colID):
    columnNum += 26**power*(ord(C)-ord('A')+1)
    power += 1
  return columnNum

def main():
  for i in range(26):
    for j in range(26):
      columnName = chr(ord('A')+i)+chr(ord('A')+j)
      columnNum = getColumnNum(columnName)
      print(f'{columnName}: {columnNum}')

if __name__ == '__main__':
  main()