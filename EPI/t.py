def g(fn):
  def i():
    print('before')
    fn()
    print('after')
  return i

@g
def f():
  print('f')

def F():
  print('F')
F = g(F)

f()
F()