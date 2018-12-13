class BankAccount:
  def __init__(self, type):
    self.type = type
    self.balance = 0
    self.overdraft_fees = 0
    self.interest_rate = .02

  def __str__(self):
    return "Bank Account type is " + self.type

  def __add__(self, other):
    return self.balance + other.balance

  def withdraw(self, amount):
    if(self.balance < amount):
      self.overdraft_fees += 20
      return False
    self.balance -= amount
    return self.balance

  def deposit(self, amount):
    if amount <= 0:
      return False
    self.balance += amount
    return self.balance

  def accumulate_interest(self):
    self.balance = self.balance + (self.balance * self.interest_rate)
    return self.balance

class ChildrensAccount(BankAccount):
  def __init__(self):
    super().__init__('account')
    self.interest_rate = 0

  def accumulate_interest(self):
    self.balance+=10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self):
    super().__init__('overdraft')
    self.overdraft_penalty = 40

  def withdraw(self, amount):
    if super().withdraw(amount):
      return self.balance
    else:
      self.balance -= self.overdraft_penalty
      return self.balance

  def accumulate_interest(self):
    if(self.balance > 0):
      return super().accumulate_interest()



basic_account = BankAccount('savings')
basic_account.deposit(600)
print(f"Basic account has ${basic_account.balance}")
basic_account.withdraw(17)
print(f"Basic account has ${basic_account.balance}")
basic_account.accumulate_interest()
print(f"Basic account has ${basic_account.balance}")
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print(f"Child's account has ${childs_account.balance}")
childs_account.withdraw(17)
print(f"Child's account has ${childs_account.balance}")
childs_account.accumulate_interest()
print(f"Child's account has ${childs_account.balance}")
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}")

print(str(basic_account))
print(f"Sum of balance of two accounts {overdraft_account + childs_account}")

# print(help(overdraft_account))