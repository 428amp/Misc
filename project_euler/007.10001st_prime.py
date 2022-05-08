from Utilities import is_prime

def main():
  ct = 0
  i = 2
  while ct < 10001:
    if is_prime(i):
      ct += 1
    i += 1
  print(i-1)

if __name__ == "__main__":
  main()