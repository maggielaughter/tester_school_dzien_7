class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            raise ValueError('Yout account must have positive number')
        self.balance=balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('You want withdraw to much money!')
        if amount <= 0:
            raise ValueError('There is no positive number')
        return self.balance-amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('There is no positive number')
        return self.balance+amount

account=BankAccount(100)
account2=BankAccount(260)
print('Konto po wypłacie :', account.withdraw(50))
print('Konto po wpłacie :', account2.deposit(40))