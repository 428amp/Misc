from LinkedStack import LinkedStack as Stack

def isMatched(expr):
  lefty = '({['
  righty = ')}]'
  S = Stack()
  for c in expr:
    if c in lefty:
      S.push(c)
    elif c in righty:
      if S.isEmpty():
        return False
      if righty.index(c) != lefty.index(S.pop()):
        return False
  return S.isEmpty()

if __name__ == '__main__':
  s = '(((((((((([[[[{{{[[]]}}}]]]]))))))))))'
  print(isMatched(s))