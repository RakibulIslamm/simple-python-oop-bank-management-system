from User import *

class Bank:
    def __init__(self, name, address, balance) -> None:
        self.bank_name = name
        self.address = address
        self.__balance = balance
        self.__total_loan = 0
        self.__customers = []
        self.__admins = []
        self.__loan_on = True

    def create_user_account(self, name, email, phone, initial_balance):
        ac_no = f'21303101250{len(self.__customers)+1}'
        customer = Customer(name, email, phone, ac_no)
        self.__customers.append(customer)
        customer.deposit(initial_balance, 'opening deposit')
        self.__balance += initial_balance
        print(f'Account created successfully. Your account number is {ac_no}')
        print(customer)
    
    def deposit(self, ac_no, amount):
        if amount > 0:
            user = self.find_a_user(ac_no)
            if user:
                user.deposit(amount)
                self.__balance += amount
            else:
                print('No user found')
        else:
            print(f"Invalid amount {amount}")


    def withdraw(self, ac_no, amount):
        user = self.find_a_user(ac_no)
        if user:
            if amount <= user.balance:
                if self.__balance >= amount:
                    user.withdraw(amount)
                    self.__balance -= amount
                else:
                    print("The bank is bankrupt")
            else:
                print(f"You havn't enough balance to withdraw {amount}, You have only {user.my_balance}")
        else:
            print('No user found')

    def get_balance(self, ac_no):
        user = self.find_a_user(ac_no)
        if user:
            print(f'Your available balance is: ৳{user.my_balance}')
        else:
            return 'User not found'
        
    def get_transactions(self, ac_no):
        user = self.find_a_user(ac_no)
        if user:
            print('****Transaction History****')
            user.my_transactions()
        else:
            return 'User not found'
        
    def transfer_balance(self, sender_ac_no, receiver_ac_no, amount):
        sender = self.find_a_user(sender_ac_no)
        receiver = self.find_a_user(receiver_ac_no)
        if sender and receiver:
            if sender.my_balance > amount:
                sender.transfer_balance(amount, receiver)
                print(f'৳{amount} transfered successfully to {receiver.name}')
            else:
                print(f"You haven't enough amount to transfer {amount}, Your current baance is {sender.my_balance}" )
        else:
            print('Your account number or Receiver account is wrong')

    def take_loan(self, ac_no, amount):
        if self.__loan_on:
            user = self.find_a_user(ac_no)
            if (amount+user.loan) <= (user.balance * 2):
                if user:
                    if amount <= self.__balance :
                        user.take_loan(amount)
                        self.__total_loan += amount
                        print(f'৳{amount} Loan received successfully!')
                    else:
                        print('Bank is goribs')
            else:
                print("Invalid amount, You will get loan only 2 times of your balance")
        else:
            print('Sorry, unfortunately the loan feature is off currently')

    def check_loan_balance(self, ac_no):
        user = self.find_a_user(ac_no)
        if user:
            print(f'Your current loan balance is: ৳{user.loan}')
        else:
            return 'User not found'

    
    def create_admin_account(self, name, email, phone):
        id = f'ABCD-0{len(self.__admins)+1}'
        admin = Admin(name, email, phone, id)
        self.__admins.append(admin)
        print(f'Admin account created with this id: {id}')

    def total_balance(self, admin_id):
        admin = self.find_an_admin(admin_id)
        if admin and admin.role == 'admin':
            print(f'Total balance of the Bank "{self.bank_name}" is ৳{self.__balance}')
        else:
            print('You are not an admin')

    def loan_feature(self, admin_id, isOn):
        admin = self.find_an_admin(admin_id)
        if admin and admin.role == 'admin':
            self.__loan_on = isOn

    def check_total_loan_balance(self, admin_id):
        admin = self.find_an_admin(admin_id)
        if admin and admin.role == 'admin':
            print(f'Total loan balance of the Bank "{self.bank_name}" is ৳{self.__total_loan}')
        else:
            print('You are not an admin')

    def find_a_user(self, ac_no):
        for user in self.__customers:
            if user.account_no == ac_no:
                return user
        return None
    
    def find_an_admin(self, id):
        for admin in self.__admins:
            if admin.id == id:
                return admin
        return None
    

# Operations

# Bank create
bank = Bank('Bangladesh Bank', 'MOTIJHEEL DHAKA-1000, 02 Dhaka, Dhaka Division', 5000)

# Create user/customer account
bank.create_user_account('Rakibul Islam', 'rakib@gmail.com', '01234567890', 500)
print('')
bank.create_user_account('Phitron', 'phitron@gmail.com', '0342457890', 500)

print('')
# Deposit and withdraw
bank.deposit('213031012501', 50000)
bank.withdraw('213031012501', 5000)
bank.deposit('213031012501', 50000)

# Transaction History of account no: 213031012501
bank.get_transactions('213031012501')

print('')
# Check balance
bank.get_balance('213031012501')

print('')
# Take loan and check loan balance
bank.take_loan('213031012501', 10000)
bank.check_loan_balance('213031012501')

print('')
# Transaction History of account no: 213031012501
bank.get_transactions('213031012501')

print('')
# Admin account create
bank.create_admin_account('Rakib', 'rakib2@gmail.com', '01673336373')

# Check total bank balance
bank.total_balance('ABCD-01')

# Off bank loan
bank.loan_feature('ABCD-01', False)
# Total loan balance
bank.check_total_loan_balance('ABCD-01')

print('')
# request loan after loan feature off
bank.take_loan('213031012501', 10000)
print('')
# Balance before transfer
bank.get_balance('213031012501')
# Transfer balance
bank.transfer_balance('213031012501', '213031012502', 5000)
# Balance after transfer
bank.get_balance('213031012501')

print('')
# Transaction history of account no: 213031012502
bank.get_transactions('213031012502')

