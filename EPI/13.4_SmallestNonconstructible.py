def smallestNonconstructible(coins):
  coins = sorted(coins)
  maxFull = 0
  for coin in coins:
    if coin > maxFull+1:
      break
    maxFull += coin
  return maxFull+1

def main():
  import random
  coinValues = [5, 10, 25, 50]
  coins = [1]*4
  for i in range(random.randrange(8, 17)):
    coins.append(random.choice(coinValues))
  print(sorted(coins))
  print(smallestNonconstructible(coins))

if __name__ == '__main__':
  main()