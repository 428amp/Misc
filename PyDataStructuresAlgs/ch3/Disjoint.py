import importlib.util
# spec = importlib.util.spec_from_file_location("TestUtilityFunctions.py", "C:/Temp/PyDatastructures/TestUtilityFunctions.py")
# Tests = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(Tests)

def disjointM(A, B, C):
  AB = []
  for a in A:
    for b in B:
      if a == b:
        AB.append(a)
  for ab in AB:
    for c in C:
      if ab == c:
        return False
  return True

def disjoint1(A, B, C):
  for a in A:
    for b in B:
      for c in C:
        if a == b == c:
          return False
    return True

def disjoint2(A, B, C):
  for a in A:
    for b in B:
      if a == b:
        for c in C:
          if a == c:
            return False
  return True

if __name__ == '__main__':
  pass