def reverseWordsDumb(s):
  words = s.split(' ')
  for i in range(len(words)):
    words[i] = words[i][::-1]
  return ' '.join(words)

#assumption is that input string is properly formatted in form word_word_word... with
#exactly one space between words
#inplace version of reverseWords
def reverseWords(s):
  start = 0
  for i in range(len(s)):
    if s[i] == ' ':
      space = i
      for j in range(0, (space-start)//2):
        s[start+j], s[space-j-1] = s[space-j-1], s[start+j]
      start = space+1
  #deal with last word
  for j in range(0, (len(s)-start)//2):
    s[start+j], s[len(s)-j-1] = s[len(s)-j-1], s[start+j]


def main():
  import random
  wordPool = [
    'word1',
    'word2',
    'word3',
    'word4',
    'word5',
    'word6',
  ]
  for i in range(500):
    s = []
    for i in range(random.randrange(1, 500)):
      s.append(random.choice(wordPool))
    s = ' '.join(s)
    s2 = list(s)
    reverseWords(s2)
    if ''.join(s2) != reverseWordsDumb(s):
      print('reverse inplace failed')
      break
    # # print(s)
    # # print(s2)
    # print(reverseWordsDumb(s))
    # reverseWords(s2)
    # print(''.join(s2))
    # print()
  else:
    print('reverse inplace success')

if __name__ == '__main__':
  main()