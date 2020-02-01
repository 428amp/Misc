def removeDuplicates(A):
  A.sort()
  write = 1
  for read in range(1, len(A)):
    if A[read] != A[write-1]:
      A[write] = A[read]
      write += 1
  del A[write:]

def main():
  import random
  for j in range(1000):
    A = []
    app = 0
    for i in range(10):
      for i in range(random.randrange(1, 10)):
        A.append(app)
      app += 1
    # print(A)
    removeDuplicates(A)
    # print(A)
    if A != [i for i in range(10)]:
      print(A)
      break
  else:
    print('no mismatch')

if __name__ == '__main__':
  main()