####### CREATING A CLASS #####################################################
class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

####### CREATING CLASS METHOD #####################################################
    # @classmethod
    # def print_all_instances():
        #not sure how to complete the bonus...

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


####### CREATING FIRST USER #####################################################
user_lucie = BankAccount(0.01, 16000)
user_lucie.deposit(100).deposit(200).deposit(220).withdraw(15000).yield_interest().display_account_info()

####### CREATING SECOND USER #####################################################
user_wesley = BankAccount(0.1, 10)
user_wesley.deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(10).withdraw(11).yield_interest().display_account_info()
