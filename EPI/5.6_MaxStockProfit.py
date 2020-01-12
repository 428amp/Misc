def maxProfit(dailyPrices):
  currentMaxProfit = 0
  currentAbsMin = dailyPrices[0]
  for price in dailyPrices:
    if price < currentAbsMin:
      currentAbsMin = price
      continue
    bestGainThisDay = price - currentAbsMin
    if bestGainThisDay > currentMaxProfit:
      currentMaxProfit = bestGainThisDay
  return currentMaxProfit, currentAbsMin, currentAbsMin+currentMaxProfit

def main():
  import random
  dailyPrices = [random.randrange(0, 100) for i in range(25)]
  profit = maxProfit(dailyPrices)
  print(dailyPrices)
  print(profit)

if __name__ == '__main__':
  main()