import random

def checkValidParens(s, k):
  balance = 0
  for char in s:
    if char not in '()':
      return False
    elif char is '(':
      balance += 1
    elif char is ')':
      balance -= 1
    if balance < 0:
      return False
  if balance == 0:
    return True

def dumb_genMatchedParensStrings(k):
  valid = []
  pool = '()'
  for i in range(2**(2*k)):
    s = []
    for j in range(2*k):
      s.append(pool[i&1])
      i >>= 1
    # print(s)
    if checkValidParens(s, k):
      valid.append(''.join(s))
  return sorted(valid)

def dumber_genMatchedParensStrings(k):
  valid = set()
  pool = ['(', ')']*(k)
  for i in range(100000):
    random.shuffle(pool)
    c = ''.join(pool)
    if checkValidParens(c, k):
      valid.add(c)
  return sorted(list(valid))

#recursive
def genMatchedParensStrings2(k):
  pass

def genMatchedParensStrings(k):
  numL = k
  numR = k
  s = '('
  numL -= 1
  while numL > 0:
    pass

def main():
  l = dumb_genMatchedParensStrings(4)
  print(l)
  print(len(l))

if __name__ == '__main__':
  main()