from operator import index
import Utilities
import math

f_name = "p099_base_exp.txt"
def main():
  exponentials = []
  with open(f_name, "r") as f:
    ct = 0
    for line in f:
      base, exp = [int(i) for i in line.split(",")]
      exp = math.log(base)*exp
      exponentials.append(exp)
      ct += 1
      # if ct >= 10:
      #   break
  index_max = max(range(len(exponentials)), key=exponentials.__getitem__)
  print(index_max, exponentials[index_max])
  print(max(exponentials))
  
  # max_seen = 0
  # for i in range(1, len(exponentials)):
  #   if exponentials[i] > exponentials[max_seen]:
  #     max_seen = i
  # print(max(exponentials))
  # print(i, exponentials[i])

if __name__ == "__main__":
  main()