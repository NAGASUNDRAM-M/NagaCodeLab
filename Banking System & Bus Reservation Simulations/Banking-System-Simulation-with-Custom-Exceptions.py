class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,acc_name,initial_amount,): 
        self.name=acc_name
        self.balance=initial_amount
        print(f"\nAccount {self.name} created\nAccount balance={self.balance:.2f}")
    def get_balance(self):
        print(f"\nAccount '{self.name}' balance={self.balance:.2f}")
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("\nDeposite Complete")
        self.get_balance()
    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nsorry accout '{self.name}' has only balance of {self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print("\nwithdraw completed.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nwithdraw interrupted:{error}')

    def transaction(self,amount,account):
        try:
            print('\n*****\n\nBeginning transer')
            self.viable_transaction(amount)
            self.withdraw( amount)
            account.deposit(amount)
            print("\nTransaction completed!✅\n\n")
        except BalanceException as error:
            print(f'Transaction interrupted.❌{error}')


Nagasundram=BankAccount('Nagasundram',2000)
Suresh=BankAccount('Suresh',5000)
Nagasundram.get_balance()
Suresh.get_balance()
Nagasundram.deposit(500)
Suresh.deposit(1000)
Nagasundram.withdraw(3000)
Nagasundram.withdraw(1000)
Nagasundram.transaction(500,Suresh)
    



