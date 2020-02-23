import collections

#recursive by shaving off palindromic prefixes
def palindromicDecompositions(s):
  if len(s) == 1:
    return [[s]]
  prefix = []
  decompositions = []
  for i in range(len(s)-1):
    prefix.append(s[i])
    if isPalindrome(''.join(prefix)):
      t = palindromicDecompositions(s[i+1:])
      for d in t:
        decompositions.append([''.join(prefix)]+d)
  if isPalindrome(s):
    decompositions.append([s])
  return decompositions

def isPalindrome(s):
  if len(s)%2 == 0:
    return s[:len(s)//2] == s[len(s):len(s)//2-1:-1]
  else:
    return s[:len(s)//2] == s[len(s):len(s)//2:-1]

def testPalindrome(s):
  for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
      return False
  return True

def testForPalindromes2(s):
  #count
  c = collections.Counter(s)
  #check at most 1 odd# count
  return sum(v%2 for v in c.values()) <= 1

def main():
  import random
  s = '12133121'
  print(palindromicDecompositions(s))
  for i in range(1000):
    pass

if __name__ == '__main__':
  main()