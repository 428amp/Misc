def replaceRemove(s, sz):
  newSz = removeB(s, sz)
  newSz = replaceA(s, newSz)
  return newSz

def removeB(s, sz):
  end = 0
  for i in range(sz):
    if s[i] != 'b':
      s[end] = s[i]
      end += 1
  return end

def replaceA(s, sz):
  #pass through once to count As, pass again to rewrite
  Acount = 0
  for i in range(sz):
    if s[i] == 'a':
      Acount += 1
  for i in range(Acount):
    s.append(None)
  start = sz+Acount-1
  for i in range(sz-1, -1, -1):
    if s[i] == 'a':
      s[start] = 'a'
      s[start-1] = 'a'
      start -= 1
    else:
      s[start] = s[i]
    start -= 1
  return sz+Acount

def main():
  s = [char for char in 'aabbcabbcc']
  print(s)
  newSz = replaceRemove(s, len(s))
  print(s[:newSz])

if __name__ == '__main__':
  main()