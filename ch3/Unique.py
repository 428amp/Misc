def unique1(S):
  for j in range(len(S)-1):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False
  return True

def unique2(S):
  S = sorted(S)
  for i in range(1, len(S)):
    if S[i-1] == S[i]:
      return False
  return True

if __name__ == '__main__':
  lu = [1,2,3,4,5]
  ld = [1,2,3,4,5,1]
  print(unique1(lu))
  print(unique1(ld))

  print(unique2(lu))
  print(unique2(ld))