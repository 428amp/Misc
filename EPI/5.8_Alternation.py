def alternation(A):
  for i in range(len(A)):
    A[i:i+2] = sorted(A[i:i+2], reverse=i%2)

def main():
  A = [i for i in range(10)]
  print(A)
  alternation(A)
  print(A)

if __name__ == '__main__':
  main()