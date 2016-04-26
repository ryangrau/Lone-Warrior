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
    
    attack = (object1.attack + randint((-object1.attack + (int(.5 * object1.attack))),
                                       (object1.attack + (int(.5 * object1.attack)))))
    defense = (object2.defense + randint(0, (object2.defense + (int(.5 * object2.defense)))))

    finalAttack = attack - defense

    #Now that we have an attack value, time to assign it to a damage value
    if finalAttack > 0:
        damage = finalAttack
        print (str(object1.name) + " did " + str(damage) + " damage!")
        return damage
    else:
        print (str(object1.name) + " missed their attack!")
        return damage

#Object1 attacks Object2    
def battle(object1, object2):
    print("Now it's " + object1.name +"'s turn!")
    #Run the attack calculator, and subject the damage from the object's HP
    object2.HP -= attackCalc(object1, object2)
    if object2.HP <= 0 :
        print (object2.name + " has died...You goddamn murderer!!!")
    else:
        print(object2.name + " has " + str(object2.HP) + " HP left!\n")
'''
We'll just use battle1 and flip the arguments.
#Object2 attacks Object1
def battle2(object1, object2):
    print("Now it's " + object2.name +"'s turn!")
    attackCalc(object1, object2)
    if object1.HP <= 0 :
        print (object1.name + " has died...You goddamn murderer!!!")
    else:
        print(object1.name + " has " + str(object1.HP) + " HP left!")
'''
#This is be the director for the battle, determining when to run certain functions
def start(object1, object2):
    while(object1.HP > 0 and object2.HP > 0):
        battle(object1, object2)
        if object2.HP > 0:
            battle(object2, object1)    
    
