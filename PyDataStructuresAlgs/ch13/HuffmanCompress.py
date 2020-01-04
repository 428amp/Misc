import heapq
import math
encodingDictionary = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
frequencies = [
  8.17,
  1.49,
  2.20,
  4.25,
  12.70,
  2.22,
  2.02,
  6.09,
  6.97,
  0.15,
  1.29,
  4.03,
  2.41,
  6.75,
  7.51,
  1.93,
  0.10,
  5.99,
  6.33,
  9.36,
  2.76,
  0.98,
  2.56,
  0.15,
  1.99,
  0.08,
]

class Node:
  def __init__(self, key, frequency, left=None, right=None):
    self.key = key
    self.frequency = frequency
    self.left = left
    self.right = right
  
  def __lt__(self, other):
    return self.frequency < other.frequency

def genEncodingTree(d):
  Q = []
  for char in d:
    newNode = Node(char, d[char])
    heapq.heappush(Q, newNode)
  while len(Q) > 1:
    min1 = heapq.heappop(Q)
    min2 = heapq.heappop(Q)
    newNode = Node(None, min1.frequency+min2.frequency, min1, min2)
    heapq.heappush(Q, newNode)
  return heapq.heappop(Q)

def genEncodingDictionary(t, prefix):
  if not t:
    return
  genEncodingDictionary(t.left, prefix+'1')
  if t.key:
    encodingDictionary[t.key] = prefix
  genEncodingDictionary(t.right, prefix+'0')

def getFrequencyDictionary(s):
  d = {}
  for char in s:
    if char not in d:
      d[char] = 0
    d[char] += 1
  return d

def getFrequency(node):
  if not node:
    return 0
  return getFrequency(node.left) + getFrequency(node.right)

def traverse(t):
  if not t:
    return
  traverse(t.left)
  if t.key:
    print(t.key, t.frequency)
  traverse(t.right)

def huffmanEncode(s):
  encoded = s
  for char in alphabet:
    encoded = encoded.replace(char, encodingDictionary[char])
  return encoded

def huffmanDecode(s):
  reverseDictionary = {}
  for key in encodingDictionary:
    reverseDictionary[encodingDictionary[key]] = key
  curReading = ''
  decoded = ''
  for char in s:
    curReading += char
    if curReading in reverseDictionary:
      decoded += reverseDictionary[curReading]
      curReading = ''
  return decoded

def main():
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  s = ''
  for i in range(26):
    s += alphabet[i]*math.floor(100*frequencies[i])
  d = getFrequencyDictionary(s)
  keyTree = genEncodingTree(d)
  genEncodingDictionary(keyTree, '')
  message = 'thequickbrownfoxjumpedoverthelazydog'
  encoded = huffmanEncode(message)
  decoded = huffmanDecode(encoded)
  for key in encodingDictionary:
    print(key, encodingDictionary[key])
  print(message)
  print(encoded)
  print(decoded)

if __name__ == '__main__':
  main()