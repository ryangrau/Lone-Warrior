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
    
    
