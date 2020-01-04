def findBruteforce(text, pattern):
  lenT = len(text)
  lenP = len(pattern)
  for i in range(lenT-lenP+1):
    if text[i] == pattern[0]:
      for j in range(1, lenP):
        if text[i+j] != pattern[j]:
          break
      else:
        return i
  return -1

def findBruteforce2(T, P):
  n, m = len(T), len(P)
  for i in range(n-m+1):
    k = 0
    while k < m and T[i+k] == P[k]:
      k += 1
    if k == m:
      return i
  return -1

def findKnuth(text, pattern):
  lenT, lenP = len(text), len(pattern)
  if lenT == 0: return -1
  fail = calcFailureKnuth(pattern)
  j = 0
  k = 0
  while j < lenT:
    if text[j] == pattern[k]:
      if k == lenP - 1:
        return j - lenP + 1
      j += 1
      k += 1
    elif k > 0:
      k = fail[k-1]
    else:
      j += 1
  return -1

def calcFailureKnuth(pattern):
  lenP = len(pattern)
  fail = [0]*lenP
  j = 1
  k = 0
  while j < lenP:
    if pattern[j] == pattern[k]:
      fail[j] = k+1
      j += 1
      k += 1
    elif k > 0:
      k = fail[k-1]
    else:
      j += 1
  return fail

if __name__ == '__main__':
  import random
  sz = 10000
  text = ''
  for i in range(sz):
    text += str(random.randrange(0,10))
  testCt = 100
  for i in range(testCt):
    start = random.randrange(0, sz-10+1)
    patternLen = random.randrange(1, 10)
    pattern = text[start:start+patternLen]
    if findBruteforce(text, pattern) != findKnuth(text, pattern):
      print('mismatch')
  else:
    print('no mismatch in', testCt, 'tries')