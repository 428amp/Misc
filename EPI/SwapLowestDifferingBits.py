def swapLowestDifferingBits(x):
  if x & 1:
    x2 = (x+1) & ~x
    return x ^ (x2 | (x2 >> 1))
  else:
    x1 = x & (x-1)
    x2 = x ^ x1
    return x1 | (x2 >> 1)

def main():
  for i in range(33):
    print('{0:6b}\n{1:6b}\n'.format(i, swapLowestDifferingBits(i)))

if __name__ == '__main__':
  main()