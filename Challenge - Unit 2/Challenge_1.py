class BankAccount:

  def __init__(self, accountNumber, accountHolder, accountBalance=0.0):
    self.accountNumber = accountNumber
    self.accountHolder = accountHolder
    self.accountBalance = accountBalance

  def deposit(self, amount):
    if (amount > 0):
      self.accountBalance = self.accountBalance + amount
      print("Deposited : {} , New Balance {}".format(amount,
                                                     self.accountBalance))
    else:
      print("Error : Invalid deposit amount : {}. Please deposit valid amount".
            format(amount))

  def withdraw(self, amount):
    if (self.accountBalance < amount):
      print("Error : Insuffient balance {}".format(self.accountBalance))
    if (amount > 0):
      self.accountBalance = self.accountBalance - amount
      print("Withdrawed : {} , New Balance {}".format(amount,
                                                      self.accountBalance))
    else:
      print(
          "Error : Invalid withdrawal amount : {}. Please withdrawal valid amount"
          .format(amount))

  def displayBalance(self):
    print("Account Balance : {}".format(self.accountBalance))


account = BankAccount("234242343534", "Ramya", 100.0)
account.displayBalance()
account.withdraw(250)
account.deposit(50)
account.withdraw(25)
account.deposit(-100)
account.displayBalance()
