# Class: a blueprint or factory
# Attributes: characteristics of a class
# Methods: actions of a class
# Instance: a creation/representation of a class

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.first_name}")


user_ada = User("Wesley", "Wilson", 2)
print(user_ada.age)  # prints: <__main__.User object at 0x1029db4c0>
user_ada.greeting()
