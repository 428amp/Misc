from ArrayStack import ArrayStack

def reverse_file(filename):
  S = ArrayStack()
  original = open(filename)
  for line in original:
    S.push(line.rstrip('\n'))
  original.close()

  output = open('reversed_'+filename, 'w')
  while not S.is_empty():
    output.write(S.pop() + '\n')
  output.close()

if __name__ == '__main__':
  reverse_file('t.txt')