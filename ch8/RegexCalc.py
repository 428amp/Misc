import re

class Node:
  def __init__(self, data, left, right):
    self.data = data
    self.left = left
    self.right = right

class ArrayStack:
  def __init__(self):
    self.data = []

  def __len__(self):
    return len(self.data)
  
  def isEmpty(self):
    return len(self.data) == 0
  
  def push(self, e):
    self.data.append(e)
  
  def top(self):
    if self.isEmpty():
      raise IndexError('Stack is empty')
    return self.data[-1]
  
  def pop(self):
    if self.isEmpty():
      raise IndexError('Stack is empty')
    return self.data.pop()

def tokenize(s):
    s = s.replace(' ', '')
    p = r'''(?P<NUM>\d+(\.\d+)?)|(?P<OP>[()*/+-])|(?P<BAD>.+?)'''
    r = re.compile(p)
    t = r.finditer(s)
    tokens = []
    for i in t:
      if i['BAD']:
        raise ValueError('invalid character: ' + i['BAD'])
      tokens.append(i.group())
    return tokens

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def isOperator(s):
  return s in '()*/+-'

def expressionTreeFrom(tokenList):
  def popAndProcess(stop):
    while not operatorStack.isEmpty() and not stop(operatorStack.top()):
      operator = operatorStack.pop()
      right = operandStack.pop()
      left = operandStack.pop()
      operator.left = left
      operator.right = right
      operandStack.push(operator)
  operatorStack = ArrayStack()
  operandStack = ArrayStack()
  for token in tokenList:
    newNode = Node(token, None, None)
    if token == '(':
      operatorStack.push(newNode)
    elif token == ')':
      popAndProcess(lambda node : node.data == '(')
      if operatorStack.isEmpty():
        raise ValueError('() mismatch')
      else:
        operatorStack.pop()
    elif token in '+-':
      popAndProcess(lambda node : node.data == '(')
      operatorStack.push(newNode)
    elif token in '/*':
      popAndProcess(lambda node : node.data in '(+-')
      operatorStack.push(newNode)
    elif isNumber(token):
      operandStack.push(newNode)
    # print([node.data for node in operatorStack.data], [node.data for node in operandStack.data])
  popAndProcess(lambda node : False)
  # print([node.data for node in operatorStack.data], [node.data for node in operandStack.data])
  if not (operatorStack.isEmpty() and len(operandStack) == 1):
    raise ValueError('improperly formatted expression')
  return operandStack.pop()

def calc(node):
  if isNumber(node.data):
    return float(node.data)
  else:
    op = node.data
    left = calc(node.left)
    right = calc(node.right)
    if op == '*':
      return left*right
    elif op == '/':
      if right == 0:
        raise ValueError('attempt to divide by 0')
      return left/right
    elif op == '+':
      return left+right
    elif op == '-':
      return left-right

def trav(tree):
  if isNumber(tree.data):
    print(tree.data, end = '')
  else:
    print('(', end = '')
    trav(tree.left)
    print(tree.data, end = '')
    trav(tree.right)
    print(')', end = '')

if __name__ == '__main__':
  # t = Node('+', Node('1', None, None), Node('2', None, None))
  # trav(t)
  # print()
  while True:
    try:
      i = input('expression: ')
      tokens = tokenize(i)
      # print(tokens)
      e = expressionTreeFrom(tokens)
      trav(e)
      print()
      print('calc:', calc(e))
    except EOFError:
      break
    except ValueError as e:
      print(e)