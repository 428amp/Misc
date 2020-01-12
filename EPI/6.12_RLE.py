def encode(s):
  cur = s[0]
  ct = 0
  encoded = []
  for c in s:
    if c != cur:
      encoded.append(str(ct)+cur)
      cur = c
      ct = 1
    else:
      ct += 1
  encoded.append(str(ct)+cur)
  return ''.join(encoded)

#does not handle strings with numeric characters initially
def decode(s):
  i = 0
  decoded = []
  while i < len(s):
    curct = ''
    while s[i].isnumeric():
      curct += s[i]
      i += 1
    ct = int(curct)
    ch = s[i]
    decoded += [ch]*ct
    i += 1
  return ''.join(decoded)

def main():
  import random
  for i in range(1000):
    s = ''
    while(len(s) < 50):
      cur = chr(ord('a')+random.randrange(0,26))
      ct = random.randrange(1,10)
      s += cur*ct
    # print(s)
    encoded = encode(s)
    # print(encoded)
    decoded = decode(encoded)
    # print(decoded)
    if s != decoded:
      print('s != decoded')
  else:
    print('all s == decoded')

if __name__ == '__main__':
  main()