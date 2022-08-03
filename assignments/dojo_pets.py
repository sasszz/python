####### CREATING NINJA CLASS #####################################################
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

####### CREATING NINJA METHODS #####################################################
    # walks the ninja's pet invoking the pet play() method
    def walk(self): 
        self.pet.play()

    # feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()

    # cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.makeNoise()



####### CREATING PET CLASS #####################################################
class Pet:
    def __init__(self, name, type, tricks, energy, health, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
        self.noise = noise

####### CREATING PET METHODS #####################################################
    # increases the pets energy by 25
    def sleep(self):
        self.energy += 25

    # increases the pet's energy by 5 & health by 10
    def eat(self):
        self.health += 10
        self.energy += 5

    # increases the pet's health by 5
    def play(self):
        self.health += 5

    # prints out the pet's sound
    def makeNoise(self):
        print(self.noise)



######### CREATING NINJA AND PET #####################################################
cat = Pet("wesley", "black", "eat", 100, 100, "meow") # create pet first
lucie = Ninja("Lucie", "Chevreuil", "kibble", "cat food", cat) # creating ninja

lucie.walk()
cat.makeNoise()
lucie.bathe()
lucie.feed()
print(cat.health)
print(cat.energy)