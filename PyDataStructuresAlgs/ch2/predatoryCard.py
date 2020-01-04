from creditCard import CreditCard

class PredatoryCreditCard(CreditCard):
  def __init__(self, customer, bank, account, limit, apr):
    super().__init__(customer, bank, account, limit)
    self._apr = apr
  
  def charge(self, price):
    success = super().charge(price)
    if not success:
      self._balance += 5
    return success

  def process_month(self):
    if self._balance > 0:
      monthly_factor = (1 + self._apr)**(1/12)
      self._balance *= monthly_factor

if __name__ == '__main__':
  import random
  # tCard2 = CreditCard(0,1,2,3)
  # tCard = PredatoryCreditCard()
  # print(dir(tCard2))
  # print()
  # print(dir(tCard))

  wallet = [
    CreditCard('name1', 'bank1', '1234 5678 9012 3456', 1000),
    CreditCard('name1', 'bank2', '6123 4567 8901 2345', 1000),
    CreditCard('name1', 'bank3', '5612 3456 7890 1234', 1000),
    PredatoryCreditCard('name1', 'bank4', '5612 3456 7890 1234', 1000, .10),
  ]

  for val in range(10):
    for card in wallet:
      card.charge(50+val*5)
      # card.charge(random.randrange(0, 100))
  for card in wallet:
    if type(card) == PredatoryCreditCard:
      card.process_month()
  for card in wallet:
    print("customer:\t", card.get_customer())
    print("bank:\t\t", card.get_bank())
    print("account:\t", card.get_account())
    print("limit:\t\t", card.get_limit())
    print("balance:\t", card.get_balance())
    print()
    while card.get_balance() > 100:
      card.make_payment(100)
      print("new_balance: ", card.get_balance())
    print()
