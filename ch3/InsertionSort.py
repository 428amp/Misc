def insertion_sort(A):
  for k in range(1, len(A)):
    cur = A[k]
    j = k
    while j > 0 and A[j-1] > cur:
      A[j] = A[j-1]
      j -= 1
    A[j] = cur

if __name__ == '__main__':
  import random
  b = [i for i in range(100)]
  l = []
  for i in range(100):
    l.insert(random.randrange(0,len(l)+1), i)
  # print(l)
  insertion_sort(l)
  # print(l)
  for i in range(100):
    if b[i] != l[i]:
      print('discrepancy')
  else:
    print('lists the same')