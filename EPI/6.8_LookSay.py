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

#version using itertools.groupby
import itertools
def lookSay2(n):
  ls = '1'
  for i in range(n):
    cur = []
    curBreakdown = itertools.groupby(ls)
    for key, group in curBreakdown:
      cur.append(str(len(list(group)))+str(key))
    ls = ''.join(cur)
  return ls


def main():
  for i in range(15):
    if lookSay(i) != lookSay2(i):
      print('diff')
      break
  else:
    print('no diff')

if __name__ == '__main__':
  main()