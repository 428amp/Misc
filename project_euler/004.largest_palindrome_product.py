from Utilities import is_palindrome

def main():
  largest_palindrome_seen = 0
  for a in range(100, 1000):
    for b in range(a, 1000):
      ab = a*b
      if ab > largest_palindrome_seen and is_palindrome(ab):
        largest_palindrome_seen = ab
  print(largest_palindrome_seen)

if __name__ == "__main__":
  main()