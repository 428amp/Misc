import collections
letters = [chr(ord('a')+i) for i in range(26)]

def testForPalindromes(s):
  d = {}
  for letter in s:
    if letter not in d:
      d[letter] = 1
    else:
      d[letter] += 1
  seenOdd = False
  for key in d:
    if d[key]%2 != 0:
      if seenOdd:
        return False
      else:
        seenOdd = True
  return True

#using collections.Counter() for condensed code
def testForPalindromes2(s):
  #count
  c = collections.Counter(s)
  #check at most 1 odd# count
  return sum(v%2 for v in c.values()) <= 1


def main():
  import random
  for i in range(10000):
    word = []
    for i in range(random.randrange(1, 10)):
      word.append(random.choice(letters))
    roll = random.randrange(0, 2)
    word += [random.choice(letters)]*roll + word[::-1]
    word = ''.join(word)
    if not testForPalindromes2(word):
      print(word)
      break
  else:
    print('all palindromes')
    
if __name__ == '__main__':
  main()