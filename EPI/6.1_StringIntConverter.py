def ItoS(I):
  if I == 0:
    return '0'
  digs = '0123456789'
  S = []
  R = abs(I)
  while R != 0:
    S.append(digs[R%10])
    R //= 10
  if I < 0:
    S.append('-')
  return ''.join(reversed(S))

def StoI(S):
  digs = '0123456789'
  neg = False
  if S[0] == '-':
    neg = True
    S = S[1:]
  I = 0
  for c in S:
    if c not in digs:
      return False
    I *= 10
    I += ord(c) - ord('0')
  if neg:
    I = -I
  return I

def main():
  for i in range(-1000,1000,1):
    if ItoS(i) != str(i):
      print('ItoS failed')
      break
  else:
    print('ItoS success')

  for i in range(-1000, 1000, 1):
    if StoI(str(i)) != i:
      print('StoI failed')
      break
  else:
    print('StoI success')

if __name__ == '__main__':
  main()
