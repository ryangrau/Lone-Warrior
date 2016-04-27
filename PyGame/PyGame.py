RandInt = 3

class Entity:
        name = ""
        HP = int
        Attack = int
        Defence = int
        RandInt = 7
        
        def printClass( self ):
            print(self.name)
            print(self.HP)
            print(self.Attack)
            print(self.Defence)
            print(self.RandInt)
            return
        



Wolf1 = Entity()
Wolf1.name = "Kujo"
Wolf1.HP = 60
Wolf1.Attack = 15
Wolf1.Defence = 2

Wolf2 = Entity()
Wolf2.name = "Fluffy"
Wolf2.HP = 80
Wolf2.Attack = 10
Wolf2.Defence = 1

Hero = Entity()
Hero.name = "Ryan"
#Will get hero name in game like this: Hero.name = raw_input("What is your name lone explorer?")
Hero.HP = 150
Hero.Attack = 12
Hero.Defence = 3

Boss = Entity()
Boss.name = "Bob"
Boss.HP = 170
Boss.Attack = 10
Boss.Defence = 6

#Wolf1.printClass()


#print(RandInt)

print("Oh no, wolves are fighting")

def battle1(object1, object2):
    print("Now it's " + object1.name +"'s turn!")
    object2.HP = object2.HP - (object1.Attack - object2.Defence)
    print(object1.name + " attacked " + object2.name + " for " + str(object1.Attack - object2.Defence) + " of damage!\n")
    if object2.HP <= 0 :
        print (object2.name + " has died...You goddamn murderer!!!")
    else:
        print(object2.name + " has " + str(object2.HP) + " HP left!")

def battle2(object1, object2):
    print("Now it's " + object2.name +"'s turn!")
    object1.HP = object1.HP - (object2.Attack - object1.Defence)
    print(object2.name + " attacked " + object1.name + " for " + str(object2.Attack - object1.Defence) + " of damage!\n")
    if object1.HP <= 0 :
        print (object1.name + " has died...You goddamn murderer!!!")
    else:
        print(object1.name + " has " + str(object1.HP) + " HP left!")


def start(object1, object2):
    while(object1.HP > 0 and object2.HP > 0):
        battle1(object1, object2)
        if object2.HP <= 0:
            break
        battle2(object1, object2)

print("Who do you want to see fight?\nWe have our hero Ryan,\na wolf named Kujo\nA dog named Fluffy\nAnd a badass named Bob")
print("\nType the two names you want to have fight.\n")
player1 = raw_input()
if player1 == Wolf1.name:
    player1 = Wolf1
elif player1 == Wolf2.name:
    player1 = Wolf2
elif player1 == Hero.name:
    player1 = Hero
elif player1 == Boss.name:
    player1 = Boss
else:
    print("\nThat's not a correct name\n")
    
print("\nNow give me the second contestant.\n")
player2 = raw_input()
if player2 == Wolf1.name:
    player2 = Wolf1
elif player2 == Wolf2.name:
    player2 = Wolf2
elif player2 == Hero.name:
    player2 = Hero
elif player2 == Boss.name:
    player2 = Boss
else:
    print("\nThat's not a correct name\n")
print("Alright, let's do this. " + object1 + " and " + object2 + " \nget out there and fight to the death\n"

start(player1, player2)
