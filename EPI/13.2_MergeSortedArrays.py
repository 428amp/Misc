#merge 2 sorted lists (arrays) with O(1) space complexity
#assume the first list has EXACTLY enough space to hold both once merged
def merge(A1, A2):
  lenA1 = 0
  while A1[lenA1] != None:
    lenA1 += 1
  for i in range(lenA1):
    A1[len(A2)+i] = A1[i]
  head1 = len(A2)
  head2 = 0
  i = 0
  while head1 < len(A1) and head2 < len(A2):
    if A1[head1] <= A2[head2]:
      A1[i] = A1[head1]
      A1[head1] = None
      head1 += 1
    else:
      A1[i] = A2[head2]
      head2 += 1
    i += 1
  while head1 < len(A1):
    A1[i] = A1[head1]
    head1 += 1
    i += 1
  while head2 < len(A2):
    A1[i] = A2[head2]
    head2 += 1
    i += 1

def main():
  A1 = [i for i in range(10)]+[None]*10
  A2 = [i for i in range(25, 35)]
  merge(A1, A2)
  print(A1)

if __name__ == '__main__':
  main()