def deleteDuplicates(A):
  cur = 0
  for i in range(1, len(A)):
    if A[i] == A[cur]:
      A[i] = None
    else:
      cur += 1
      if cur != i:
        A[cur] = A[i]
        A[i] = None
  return cur

def main():
  import random
  # A = []
  # for i in range(16):
  #   A.append(random.randrange(10))
  # A.sort()
  # print(A)
  # B = list(set(A))
  # e = deleteDuplicates(A)
  # print(A)
  # print(A[:e+1])
  # print(B)

  for i in range(1000):
    A = []
    for i in range(16):
      A.append(random.randrange(10))
    A.sort()
    B = list(set(A))
    e = deleteDuplicates(A)
    if A[:e+1] != B:
      print('deleteDuplicates failed')
      break
  else:
    print('deleteDuplicates success')

if __name__ == '__main__':
  main()