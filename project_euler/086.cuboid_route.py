from Utilities import is_square

"""
given 3 dimensions of cuboid, derive 3 shortest path candidates
preload pythagorean triples
decompose triples into potential cuboids
a=k(m**2-n**2) b=k*2mn c=k(m**2+n**2)

conjecture: in cuboid w/ dims a,b,c with a<=b<=c shortest path is (a+b), c for legs of triangle
proof from leg cases:
  a+b, c, sqrt(a**2+b**2+c**2+2ab
  a+c, b, sqrt(a**2+b**2+c**2+2ac
  b+c, a, sqrt(a**2+b**2+c**2+2bc

otherwise iterate l, w, h w/ l<=w<=h
"""

#PARAMS
M = 1818
mn_range = int((2*M)**.5)+1 #decide exact bounds (+/-1 etc)
m_range, n_range, k_range = mn_range, mn_range, M//3+1

def gen_pythagorean_triples():
  triples = set()
  for n in range(1, n_range):
    for m in range(n+1, m_range):
      for k in range(1, k_range):
        a = k*(m**2-n**2)
        b = k*2*m*n
        c = k*(m**2+n**2)
        triples.add(tuple(sorted((a,b,c))))
  return list(triples)

def count_valid_cuboids(triple, M):
  """
  given pythag triple (a,b,c) count # of valid cuboids w/ c as shortest path
  extra condition max length M of any dim of cuboid
  """
  a, b, c = triple
  ct = 0
  #(1 to a//2, a-, b) and (b//2 to a, b-, a)
  #case1
  if M < b:
    pass
  else:
    ct += a//2

  #case2
  if M < a:
    pass
  else:
    if b-b//2 <= a and b-b//2 <= M:
      if M < a:
        ct += M-(b-b//2)+1
      else:
        ct += a-(b-b//2)+1

  return ct

def count_cuboid_routes(M):
  """
  brute force route ct used for verifying other fns work
  """
  def valid_cuboid(l, w, h):
    """returns if """
    return is_square((l+w)**2+h**2)
  ct = 0
  for l in range(1, M+1):
    for w in range(l, M+1):
      for h in range(w, M+1):
        dims = (l, w, h)
        ct += valid_cuboid(l, w, h)
  return ct

##DEPRECATED FUNCTIONS
# def get_diags(cuboid):
#   diag = lambda a, b: (a**2+b**2)**.5
#   l, w, h = cuboid
#   diag1 = diag(l+w, h)
#   diag2 = diag(l+h, w)
#   diag3 = diag(w+h, l)
#   print(l+w, h, diag1)
#   print(l+h, w, diag2)
#   print(w+h, l, diag3)

# def decompose_triple(triple):
#   """
#   given pythag triple (a,b,c) derive all possible cuboids w/ c as shortest path on long diag
#   """
#   #either (n, a-n, b) or (n, b-n, a)
#   a, b, c = triple
#   for n in range(1, a//2+1):
#     print(n, a-n, b)
#     print(get_potential_shortest(n, a-n, b))

# def get_potential_shortest(l, w, h):
#   """
#   given cuboid dim (l,w,h) gets shortest path out of 3 candidates
#   only cares if shortest path length is integer
#   """
#   def get_diag_sq(a, b):
#     return a**2+b**2
#   d1 = get_diag_sq(l+w, h)
#   d2 = get_diag_sq(l+h, w)
#   d3 = get_diag_sq(w+h, l)
#   smallest = min(d1, d2, d3)
#   if not is_square(smallest):
#     return -1
#   else:
#     return int(smallest**.5)

def main():
  # c = count_cuboid_routes(99)
  # print(c)

  triples = gen_pythagorean_triples()
  i = 0
  ct = 0
  while True:
    if i == len(triples):
      break
    triple = triples[i]
    # print(triple)
    cuboids = count_valid_cuboids(triple, M)
    ct += cuboids
    i += 1
  print(f"M={M}, ct={ct}")

  # while triples[i][2] <= 100:
  #   triple = triples[i]
  #   print(triple)
  #   ct += count_valid_cuboids(triple, 100)
  #   i += 1
  # print(ct, triples[i-1][2])

  # t = (60, 80, 100)
  # print(count_valid_cuboids(t, 100))
  # c = (2,6,6)
  # print(get_diags(c))

if __name__ == "__main__":
  main()