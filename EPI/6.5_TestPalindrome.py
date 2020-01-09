def testPalindrome(s):
  for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
      return False
  return True

def main():
  import random
  for i in range(1000):
    s = []
    for i in range(random.randrange(1, 10)):
      s.append(chr(ord('a') + random.randrange(0, 26)))
    s += s[::-1]
    if not testPalindrome(s):
      print('testPalindrome error')
      break
  else:
    print('testPalindrome success')

if __name__ == '__main__':
  main()