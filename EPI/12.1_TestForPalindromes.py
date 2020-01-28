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

def main():
  import random
  for i in range(10000):
    word = []
    for i in range(random.randrange(1, 10)):
      word.append(random.choice(letters))
    roll = random.randrange(0, 2)
    word += [random.choice(letters)]*roll + word[::-1]
    word = ''.join(word)
    if not testForPalindromes(word):
      print(word)
      break
  else:
    print('all palindromes')
    
if __name__ == '__main__':
  main()