#Prints the array 
def printArr(a, n): 
    for i in range(n): 
        print(a[i],end=" ") 
    print() 
  
# Generating permutation using Heap Algorithm 
def heapPermutation(a, size, n): 
      
    # if size becomes 1 then prints the obtained 
    # permutation 
    if (size == 1): 
        printArr(a, n) 
        return
  
    for i in range(size): 
        heapPermutation(a,size-1,n); 
  
        # if size is odd, swap first and last 
        # element 
        # else If size is even, swap ith and last element 
        if size&1: 
            a[0], a[size-1] = a[size-1],a[0] 
        else: 
            a[i], a[size-1] = a[size-1],a[i] 

def swap(elements, i, j):
    elements[i], elements[j] = elements[j], elements[i]

def generate_permutations(elements, n):
  # As by Robert Sedgewick in Permutation Generation Methods
  c = [0] * n
  yield elements
  i = 0
  while i < n:
    if c[i] < i:
      if i % 2 == 0:
        swap(elements, 0, i)
      else:
        swap(elements, c[i], i)
      yield elements
      c[i] += 1
      i = 0
    else:
      c[i] = 0
      i += 1

def permutations(elements):
  return generate_permutations(elements, len(elements))

def permutations1(n, A):
    if n == 1:
        yield A
        return

    # print(A, n)
    yield from permutations1(n-1, A)

    even = True if n%2 == 0 else False
    for i in range(n-1):
        if even:
            swap(A, i, n-1)
        else:
            swap(A, 0, n-1)
        yield from permutations1(n-1, A)
        # print(A, n)

if __name__ == '__main__':
  # elements = [i for i in range(4)]
  # ct = 0
  # for i in permutations1(4, elements):
  #   ct += 1
  #   print(i)
  # print(ct)
  # ct = 0
  # for i in permutations(elements):
  #   ct += 1
  #   print(i)
  # print('ct', ct)
  a = [i for i in range(4)] 
  n = len(a) 
  heapPermutation(a, n, n) 