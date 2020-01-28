import collections
letters = 'abcdefghijklmnopqrstuvwxyz'

def dumb_checkAnagrams(w1, w2):
  return sorted(w1) == sorted(w2)

def checkAnagrams(w1, w2):
  ct = [0]*26
  for letter in w1:
    ct[ord(letter)-ord('a')] += 1
  for letter in w2:
    ct[ord(letter)-ord('a')] -= 1
  return ct == [0]*26

def hash(s):
  h = [0]*26
  for letter in s:
    h[ord(letter)-ord('a')] += 1
  return '/'.join([str(c) for c in h])

def findAnagrams(strings):
  d = collections.defaultdict(list)
  for string in strings:
    d[hash(string)].append(string)
  return d

def main():
  import random
  # for i in range(10000):
  #   word = []
  #   for i in range(random.randrange(5,20)):
  #     word.append(letters[random.randrange(0, 26)])
  #   shuffled = word[:]
  #   random.shuffle(shuffled)
  #   ''.join(word)
  #   ''.join(shuffled)
  #   if not checkAnagrams(word, shuffled):
  #     print(word, shuffled)
  #     break
  # else:
  #   print('all anagrams')

  fail = False
  for i in range(100):
    strings = []
    while len(strings) < 50:
      word = random.sample(letters, k=random.randrange(5, 15))
      for i in range(random.randrange(1, 10)):
        strings.append(''.join(word))
        random.shuffle(word)
    d = findAnagrams(strings)
    for key in d:
      base = None
      for word in d[key]:
        if not base:
          base = sorted(word)
        else:
          if base != sorted(word):
            fail = True
  if not fail:
    print('success')

if __name__ == '__main__':
  main()
