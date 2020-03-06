#only returns length
def longestIncreasingSubarray(A):
  longest = 1
  cur = 1
  for i in range(1, len(A)):
    if A[i] > A[i-1]:
      cur += 1
    else:
      if cur > longest:
        longest = cur
      cur = 1
  return longest

#returns slice
#need to think about edge cases a little more
def longestIncreasingSubarray2(A):
  #noninclusive end
  longestStart = 0
  longestEnd = 1
  start = 0
  # longest = None
  for i in range(1, len(A)):
    if A[i] > A[i-1]:
      continue
    else:
      length = i - start - 1
      currentLongest = longestEnd - longestStart
      if length > currentLongest:
        longestStart = start
        longestEnd = i
      start = i
  return longestStart, longestEnd

#avg < 1 runthrough version
def longestIncreasingSubarray3(A):
  i = 0
  L = 1
  while i+L < len(A):
    iValid = True
    for j in range(i+L, i, -1):
      if not A[j] > A[j-1]:
        i = j
        iValid = False
        break
    if iValid:
      i += L
      while i < len(A) and A[i-1] < A[i]:
        i += 1
        L += 1
      c = i-L, i
  return c

def main():
  A = [2,11,3,5,13,7,19,17,23]
  s = longestIncreasingSubarray2(A)
  print(A[s[0]:s[1]])

  s2 = longestIncreasingSubarray3(A)
  print(A[s2[0]:s2[1]])

if __name__ == '__main__':
  main()