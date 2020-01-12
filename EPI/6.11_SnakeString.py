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

def main():
  print(snakeString('Hello World!'))

if __name__ == '__main__':
  main()