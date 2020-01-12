def dutchFlagDumb(A, ind):
  pivotValue = A[ind]
  lt = []
  eq = []
  gt = []
  for i in range(len(A)):
    if A[i] < pivotValue:
      lt.append(A[i])
    elif A[i] == pivotValue:
      eq.append(A[i])
    else:
      gt.append(A[i])
  return pivotValue, lt + eq + gt

def swap(A, i, j):
  A[i], A[j] = A[j], A[i]

#pass through and move smaller elements to left, larger to right, middle to middle
#end when smaller/larger/equal meet
def dutchFlagInPlace(A, ind):
  pivotValue = A[ind]
  smaller = 0
  equal = 0
  larger = len(A)
  while equal < larger:
    if A[equal] < pivotValue:
      swap(A, equal, smaller)
      smaller += 1
      equal += 1
    elif A[equal] == pivotValue:
      equal += 1
    else:
      larger -= 1
      swap(A, equal, larger)

# def 
def main():
  import random

  # #inplace pivot
  # A = []
  # for i in range(16):
  #   A.append(random.randrange(0, 8))
  # random.shuffle(A)
  # A2 = A.copy()
  # pivotIndex = random.randrange(0, len(A))
  # pivot, dutchFlagA = dutchFlagDumb(A, pivotIndex)
  # print(A)
  # print(dutchFlagA)
  # dutchFlagInPlace(A2, pivotIndex)
  # print(A2)
  # print(pivot)

  # #3 possible values, block 3 types together w/ each other
  # A = []
  # for i in range(16):
  #   A.append(random.randrange(0,3))
  # first1 = A.index(1)
  # print(A[first1])
  # print(A)
  # dutchFlagInPlace(A, first1)
  # print(A)

  # #2 possible values, block together
  # A = []
  # for i in range(16):
  #   A.append(random.randrange(0,2))
  # first1 = A.index(1)
  # print(A[first1])
  # print(A)
  # dutchFlagInPlace(A, first1)
  # print(A)

  #bool with 0=false, !0=true
  #block without changing relative order
  A = []
  c = 1
  for i in range(16):
    TF = random.randrange(0,2)
    if TF:
      A.append(c)
      c += 1
    else:
      A.append(0)
  first1 = A.index(1) #possible 16 0 but ignored
  print(A)
  dutchFlagInPlace(A, first1)
  print(A)

if __name__ == '__main__':
  main()