import Utilities

#largest nC2 < 2e6**.5 is when n=63
nC2 = lambda n: int(n*(n-1)/2)

def main():
  closest = float("inf")
  nC2_list = [nC2(i) for i in range(1, 2002)]
  for l in range(1, 63):
    w = l
    rect_count = nC2_list[l]*nC2_list[w]
    while rect_count < 2*10**6:
      w += 1
      rect_count = nC2_list[l]*nC2_list[w]
    # print(l, w, rect_count) #nearest over
    if abs(rect_count - 2*10**6) < closest:
      dims_closest = (l, w)
      closest = abs(rect_count - 2*10**6)
    # print(l, w-1, nC2_list[l]*nC2_list[w-1]) #nearest under
    if abs(nC2_list[l]*nC2_list[w-1] - 2*10**6) < closest:
      dims_closest = (l, w-1)
      closest = abs(nC2_list[l]*nC2_list[w-1] - 2*10**6)
  print(dims_closest, closest)

if __name__ == "__main__":
  main()