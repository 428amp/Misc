def snakeString(s):
  snaked = []
  i = 1
  while i < len(s):
    snaked.append(s[i])
    i += 4
  i = 0
  while i < len(s):
    snaked.append(s[i])
    i += 2
  i = 3
  while i < len(s):
    snaked.append(s[i])
    i += 4
  return ''.join(snaked)

#slice version
def snakeString2(s):
  return s[1::4]+s[0::2]+s[3::4]

def main():
  print(snakeString('Hello World!'))
  print(snakeString2('Hello World!'))

if __name__ == '__main__':
  main()