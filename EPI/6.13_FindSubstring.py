def find(sub, s):
  #hash O(len(s)) complexity
  hashSub = sum([ord(c) for c in sub])
  hashCur = sum([ord(c) for c in s[0:len(sub)]])
  for i in range(len(s) - len(sub)):
    if hashSub == hashCur:
      if s[i:i+len(sub)] == sub:
        return i
    hashCur = hashCur - ord(s[i]) + ord(s[i+len(sub)])
  #last check on s[-len(sub):]
  if s[-len(sub):] == sub:
    return len(s) - len(sub)
  return -1

#worst case O(n^2)
def findDumb(sub, s):
  for i in range(len(s)):
    if s[i] == sub[0]:
      if s[i:i+len(sub)] == sub:
        return i
  return -1

def main():
  import random
  s = 'string with string'
  sub = 'sub'
  for i in range(1000):
    insertIndex = random.randrange(0, len(s))
    sWithSub = s[:insertIndex] + sub + s[insertIndex:]
    if find(sub, sWithSub) != sWithSub.find(sub):
      print('find mismatch')
      break
  else:
    print('no find mismatch')

if __name__ == '__main__':
  main()