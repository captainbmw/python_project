from abc import ABC, abstractmethod



# Encapsulation
class Account:
    def __init__(self, account_id,holder_name,balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} new balance to {self.balance}")
    def withdraw(self, amount):

        print(f"Withdrawing {amount} new balance to {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} balance to {self.balance}")
        else:
            print("Insufficient  funds to withdraw")

    def check_balance(self):
        return self.balance
    def get_holder_name(self):
        return self.holder_name
# inheritance
class Customer(Account):
    def __init__(self, account_id, holder_name, balance,phone_number):
        super().__init__( account_id, holder_name,balance)
        self.phone_number = phone_number

# polymorphism
class Transaction():
    def __init__(self,amount):
        self.amount = amount
    def execute(self,account):
        pass

class DepositTransaction(Transaction):
    def execute(self,account):
        account.deposit(self.amount)

class WithdrawTransaction(Transaction):
    def execute(self,account):
        account.withdraw(self.amount)

# Abstraction
class Payment(ABC):
    @abstractmethod
    def process_transaction(self,amount):
        pass

class MpesaPaymentSystem(Payment):
    def process_transaction(self,amount):
        print(f"Processing Mpesa payment of {amount}")

# Example usage
mpesa=MpesaPaymentSystem()
account1=Customer(1,"Captain bmw",2000,723456678)
deposit=DepositTransaction(500)
withdraw=WithdrawTransaction(1200)

deposit.execute(account1)
withdraw.execute(account1)

print(f"Balance for {account1.get_holder_name()} is:"
      f"{account1.check_balance()}")

account2=Customer(2,"Hanniah",500000,74567879)
deposit=DepositTransaction(1000)
withdraw=WithdrawTransaction(1200)
deposit.execute(account2)
withdraw.execute(account2)
print(f"Balance for {account2.get_holder_name()} is:"
      f"{account2.check_balance()}")