import collections

def letterConstructible(letter, magazine):
  c1 = collections.Counter(letter)
  c2 = collections.Counter(magazine)
  return not c1 - c2

def dumb_letterConstructible(letter, magazine):
  c1 = collections.Counter(letter)
  for c in magazine:
    if c in c1:
      c1[c] -= 1
      if c1[c] == 0:
        del c1[c]
        if not c1:
          return True
  return False

def main():
  import random
  for i in range(1000):
    with open('MSND.txt') as f:
      f.seek(random.randrange(0, 1000))
      magazine = f.read(2000)
    with open('MSND2.txt') as f:
      f.seek(random.randrange(0, 1000))
      letter = f.read(random.randrange(100, 500))
    lC = letterConstructible(letter, magazine)
    dlC = dumb_letterConstructible(letter, magazine)
    if lC != dlC:
      print('mismatch')
      break
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()