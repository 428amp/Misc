class CreditCard:
  """credit card test class"""
  def __init__(self, customer, bank, account, limit):
    """
    attributes
      customer  name of customer
      bank      name of bank
      acnt      numerical account identifier
      limit     credit limit in dollars
      balance   account balance default 0  
    """
    self._customer = customer
    self._bank = bank
    self._account = account
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    return self._customer
  
  def get_bank(self):
    return self._bank

  def get_account(self):
    return self._account

  def get_limit(self):
    return self._limit
  
  def get_balance(self):
    return self._balance
  
  def charge(self, price):
    if price + self._balance > self._limit:
      return False
    self._balance += price
    return True
  
  def make_payment(self, amount):
    self._balance -= amount

if __name__ == '__main__':
  import random
  wallet = [
    CreditCard('name1', 'bank1', '1234 5678 9012 3456', 1000),
    CreditCard('name1', 'bank2', '6123 4567 8901 2345', 1000),
    CreditCard('name1', 'bank3', '5612 3456 7890 1234', 1000),
  ]

  for val in range(10):
    for card in wallet:
      card.charge(random.randrange(0, 100))
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

  

