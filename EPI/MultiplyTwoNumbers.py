def product(m, n):
  '''
  m, n positive integers as arrays least significant first
  '''
  product = [0] * (len(m) + len(n)) #max length
  for i in range(len(m)):
    for j in range(len(n)):
      product[i+j] += m[i] * n[j]
      product[i+j+1] += product[i+j]//10
      product[i+j] %= 10
  for i in range(len(product)-1, -1, -1):
    if product[i] == 0:
      product = product[:-1]
    else:
      break
  return product

def AtoD(d):
  '''
  reversed integer array to int
  '''
  p = 0
  n = 0
  for i in range(len(d)):
    n += d[i]*10**p
    p += 1
  return n

def DtoA(d):
  '''
  int to reversed integer array
  '''
  return [int(c) for c in reversed(str(d))]

def main():
  for i in range(100):
    for j in range(1000):
      a = DtoA(i)
      b = DtoA(j)
      p = AtoD(product(a, b))
      if p != i*j:
        print('incorrect product calc')
  else:
    print('no incorrect product calcs')

if __name__ == '__main__':
  main()