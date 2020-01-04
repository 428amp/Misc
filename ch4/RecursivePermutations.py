def Perm(seq, size):
  if size == 1:
    return [[e] for e in seq]
  perms = []
  for element in seq:
    tempSeq = seq.copy()
    tempSeq.remove(element)
    smallerPermList = Perm(tempSeq, size-1)
    for perm in smallerPermList:
      perms.append([element] + perm)
  return perms

def Perm2(seq, size):
  for element in seq:
    pass
  
if __name__ == '__main__':
  print(len(Perm([1,2,3,4,5], 3)))