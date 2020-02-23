import random
def greyCode(n):
  greyCode = [random.randrange(0, 2**n)]
  for i in range(1, 2**n):
    j = 0
    cur = greyCode[i-1]^(2**j)
    while cur in greyCode:
      j += 1
      cur = greyCode[i-1]^(2**j)
    greyCode.append(cur)
  return greyCode

def main():
  l = greyCode(4)
  if sorted(l) != [i for i in range(2**4)]:
    print('mismatch')
  for n in l:
    print(f'{n:04b}')

if __name__ == '__main__':
  main()