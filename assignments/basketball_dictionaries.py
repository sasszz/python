####### BBALL PLAYER DICTIONARY #####################################################
# the following is a [list] of {dictionaries}
players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

####### BBALL PLAYER CLASS #####################################################
# Challenge 1: Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.

class Player: #My attempt at Challenge #1 - it works!!
    def __init__(self, some_list, i):
        self.name = some_list[i]["name"]
        self.age = some_list[i]["age"]
        self.position = some_list[i]["position"]
        self.team = some_list[i]["team"]


# CHALLENGE 2: Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.

kevin = Player(players, 0)
print(kevin.name)
jason = Player(players, 1)
print(jason.name)
kyrie = Player(players, 2)
print(kyrie.name)

# CHALLENGE 3: Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.