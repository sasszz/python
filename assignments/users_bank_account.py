####### CREATING BANK ACCOUNT CLASS #####################################################
class BankAccount:
    number_of_accounts = 0
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.add_bank_account()

####### CREATING CLASS METHODS #####################################################
    @classmethod
    def print_all_instances(cls):
        return cls.number_of_accounts

    @classmethod
    def add_bank_account(cls):
        cls.number_of_accounts += 1

####### CREATING METHODS #####################################################
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient Funds")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance < 0:
            print("Error, $0 balance")
            return self
        self.balance += self.balance * self.int_rate
        return self


# ####### CREATING FIRST USER #####################################################
# user_lucie = BankAccount(0.01, 16000)
# user_lucie.deposit(100).deposit(200).deposit(220).withdraw(
#     15000).yield_interest().display_account_info()

# ####### CREATING SECOND USER #####################################################
# user_wesley = BankAccount(0.1, 10)
# user_wesley.deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(
#     10).withdraw(11).yield_interest().display_account_info()

print(BankAccount.print_all_instances())

####### CREATING USER CLASS #####################################################
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checking": BankAccount(int_rate=0.0, balance=0), "savings": BankAccount(int_rate=0.02, balance=0)}

####### CREATING METHODS #####################################################
    def make_deposit(self, account_type, amount):
        self.account[account_type].deposit(amount)		# we can call the BankAccount instance's methods
        print(self.account[account_type].balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)		# we can call the BankAccount instance's methods
        print(self.account.balance)
        return self

    def check_account_info(self):
        print(self.account.balance)
        return self

######### CREATING FIRST USER #####################################################
lucie = User("Lucie", "lu@cie.com")
# lucie.make_deposit(20).check_account_info()
lucie.make_deposit("checking", 20)