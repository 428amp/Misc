keyMap = (
  '0',
  '1',
  'ABC',
  'DEF',
  'GHI',
  'JKL',
  'MNO',
  'PQRS',
  'TUV',
  'WXYZ',
)

keyMap2 = (
  '0___',
  '1___',
  'ABC_',
  'DEF_',
  'GHI_',
  'JKL_',
  'MNO_',
  'PQRS',
  'TUV_',
  'WXYZ',
)

#find all possible "words" equivalent to the passed 7-digit phone#
#phone# passed as string
#recursive version
def computePnemonics(N):
  def helper(d):
    if d == len(N):
      P.append(''.join(cur))
    else:
      for c in keyMap[int(N[d])]:
        cur[d] = c
        helper(d+1)
  
  P = []
  cur = [0]*len(N)
  helper(0)
  P.sort()
  return P

#count base4
def computePnemonics2(N):
  P = []
  digits = [int(d) for d in N]
  for i in range(2**14):
    cur = []
    has_ = False
    for j in range(7):
      if keyMap2[digits[j]][i&3] == '_':
        has_ = True
        break
      cur.append(keyMap2[digits[j]][i&3])
      i >>= 2
    if not has_:
      P.append(''.join(cur))
  P.sort()
  return P

#nest 7 times
def computePnemonicsDumb(N):
  P = []
  digits = [int(d) for d in N]
  for d1 in keyMap[digits[0]]:
    for d2 in keyMap[digits[1]]:
      for d3 in keyMap[digits[2]]:
        for d4 in keyMap[digits[3]]:
          for d5 in keyMap[digits[4]]:
            for d6 in keyMap[digits[5]]:
              for d7 in keyMap[digits[6]]:
                P.append(d1+d2+d3+d4+d5+d6+d7)
  P.sort()
  return P

def main():
  t = '2276696'
  P1 = computePnemonicsDumb(t)
  P2 = computePnemonics2(t)
  P3 = computePnemonics(t)
  eq = False
  if P1 == P2:
    if P2 == P3:
      eq = True
  print(eq)

if __name__ == '__main__':
  main()