#valid ip in form a.b.c.d where a,b,c,d each 0-255
#just try len 1,2,3 for each section
def getValidIPs(s):
  def valid(n):
    if not n.isnumeric():
      return False
    return (0 <= int(n) <= 255)
  valids = []
  for s1 in range(1, 4):
    pre1 = s[:s1]
    if not valid(pre1):
      continue
    for s2 in range(s1+1, s1+4):
      pre2 = s[s1:s2]
      if not valid(pre2):
        continue
      for s3 in range(s2+1, s2+4):
        pre3 = s[s2:s3]
        if not valid(pre3):
          continue
        for s4 in range(s3+1, s3+4):
          suff = s[s3:s4]
          if not valid(suff):
            continue
          address = '.'.join([pre1,pre2,pre3,suff])
          valids.append(address)
  return valids

def main():
  L = getValidIPs('19216811')
  L.sort()
  for a in L:
    print(a)

if __name__ == '__main__':
  main()