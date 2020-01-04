def factors(n):
  for k in range(1, n+1):
    if n%k ==0:
      yield k

def factors2(n):
  k = 1
  while k*k < n:
    if n%k == 0:
      yield k
      yield n//k
    k += 1
  if k*k == n:
    yield k

# for f in factors(6):
#   print(f)

for f in factors(16):
  print(f)

