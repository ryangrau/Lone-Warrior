'''
Imports
'''
from random import randint

'''
***Function Creation***
'''
#The math breakdown is essentially choose a random number between
#-attack+random attack modifier to attack + randon attack modifier
def attackCalc(object1, object2):
    damage = 0
    
    attack = (object1.attack + randint((-object1.attack + (.5 * object1.attack)),
                                       (object1.attack + (.75 * object1.attack))))
    defense = (object2.defense + randint(0, (object2.defense + (.25 * object2.defense))))

    finalAttack = attack - defense

    #Now that we have an attack value, time to assign it to a damage value
    if finalAttack > 0:
        damage = finalAttack
        print (str(object1.name) + " did " + str(damage) + "!")
        return damage
    else:
        print (str(object1.name) + " missed their attack!")
        return damage

#Object1 attacks Object2    
def battle1(object1, object2):
    print("Now it's " + object1.name +"'s turn!")
    object2.HP = object2.HP - (object1.Attack - object2.Defence)
    print(object1.name + " attacked " + object2.name + " for " + str(object1.Attack - object2.Defence) + " of damage!\n")
    if object2.HP <= 0 :
        print (object2.name + " has died...You goddamn murderer!!!")
    else:
        print(object2.name + " has " + str(object2.HP) + " HP left!")

#Object2 attacks Object1
def battle2(object1, object2):
    print("Now it's " + object2.name +"'s turn!")
    object1.HP = object1.HP - (object2.Attack - object1.Defence)
    print(object2.name + " attacked " + object1.name + " for " + str(object2.Attack - object1.Defence) + " of damage!\n")
    if object1.HP <= 0 :
        print (object1.name + " has died...You goddamn murderer!!!")
    else:
        print(object1.name + " has " + str(object1.HP) + " HP left!")

#This is be the director for the battle, determining when to run certain functions
def start(object1, object2):
    while(object1.HP > 0 and object2.HP > 0):
        battle1(object1, object2)
        if object2.HP > 0:
            battle2(object1, object2)    
    
