####### CREATING A CLASS #####################################################
class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
####### CREATING METHODS #####################################################
    def display_info(self):
        print({self.first_name})
        print({self.last_name})
        print({self.email})
        print({self.age})
        print({self.gold_card_points})
    
    def enroll(self):
        if self.is_rewards_member == True:
            return
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points == 0:
            print("You have a 0 point balance")
            return
        self.gold_card_points -= amount

####### CREATING FIRST USER #####################################################
user_mango = User("Mango", "Sweetness", "MS@g.com", 2)
user_mango.enroll()
user_mango.spend_points(50)
user_mango.enroll()
user_mango.display_info()

####### CREATING SECOND USER #####################################################
user_lucie = User("Lucie", "Chevreuil", "lc@f.com", 25)
user_lucie.enroll()
user_lucie.spend_points(80)
user_lucie.display_info()

####### CREATING THIRD USER #####################################################
user_wesley = User("Wesley", "Wilson", "ww@w.com", 2)
user_wesley.display_info()
user_wesley.spend_points(20)