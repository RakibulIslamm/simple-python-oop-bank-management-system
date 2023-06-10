from Transaction import *

class User():
    def __init__(self, name, email, phone) -> None:
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self) -> str:
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone}'


class Customer(User):
    def __init__(self, name, email, phone, account_no) -> None:
        self.role = 'customer'
        self.account_no = account_no
        self.balance = 0
        self.loan = 0
        self.transaction_history = []
        self.role = 'customer'
        super().__init__(name, email, phone)


    def take_loan(self, amount):
        self.loan += amount
        transaction = Transaction(self.name, self.account_no,'loan', amount)
        self.transaction_history.append(transaction)

    def transfer_balance(self, amount, account_holder):
        if amount <= self.balance:
            account_holder.balance += amount
            self.balance -= amount
            transaction1 = Transaction(self.name, self.account_no,'transfer', amount)
            transaction2 = Transaction(self.name, self.account_no,'received', amount)
            self.transaction_history.append(transaction1)
            account_holder.transaction_history.append(transaction2)
    
    def my_transactions(self):
        for transaction in self.transaction_history:
            print(transaction)

    @property
    def my_balance(self):
        return self.balance
    
    def deposit(self, amount, type='deposit'):
        self.balance += amount
        transaction = Transaction(self.name, self.account_no,type, amount)
        self.transaction_history.append(transaction)
        # print(f'After deposit {amount}, Your new balance is {self.balance}')
            
        
    def withdraw(self, amount):
        self.balance -= amount
        transaction = Transaction(self.name, self.account_no,'widthdraw', amount)
        self.transaction_history.append(transaction)
        # print(f'After withdraw {amount}, Your new balance is {self.balance}')


class Admin(User):
    def __init__(self, name, email, phone, id_no) -> None:
        self.role = 'admin'
        self.id = id_no
        super().__init__(name, email, phone)
