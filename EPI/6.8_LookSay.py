def lookSay(n):
  ls = '1'
  lsN = []
  for i in range(n):
    curChar = ls[0]
    curCharCt = 0
    for j in ls:
      if j == curChar:
        curCharCt += 1
      else:
        lsN.append(str(curCharCt))
        lsN.append(str(curChar))
        curChar = j
        curCharCt = 1
    lsN.append(str(curCharCt))
    lsN.append(str(curChar))
    ls = ''.join(lsN)
    lsN = []
  return ls

def main():
  for i in range(10):
    print(lookSay(i))

if __name__ == '__main__':
  main()