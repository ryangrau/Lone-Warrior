'''
Imports
'''
from random import randint
import Classes

'''
***Function Creation***
'''
#The math breakdown is essentially choose a random number between
#-attack+random attack modifier to attack + randon attack modifier
#The function will do the math, then return an integer "damage"
def attackCalc(object1, object2):
    #Ensure damage is cleared to 0.
    damage = 0
    
    #Determine attack number
    attack = (object1.attack + randint((-object1.attack + (int(.5 * object1.attack))),
                                       (object1.attack + (int(.5 * object1.attack)))))
    #Determine defense number
    defense = (object2.defense + randint(0, (object2.defense + (int(.5 * object2.defense)))))

    #Calculate the difference
    finalAttack = attack - defense

    #Now that we have an attack value, time to assign it to a damage value
    #If the attack is above 0, that is our damage value
    if finalAttack > 0:
        damage = finalAttack
        print (str(object1.name) + " did " + str(damage) + " damage!")
        return damage
    #If it is below zero, we need it to be 0, otherwise we'd be healing on the opponent.
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
def runBattle(object1, object2):
    while(object1.HP > 0 and object2.HP > 0):
        battle(object1, object2)
        if object2.HP > 0:
            battle(object2, object1) 

def start(object1):
    #Include your print statements for opening narrative
    
    
    getName(object1)

    #blah blah blah, welcome hero, now choose your weapon
    
def getName(object1):
    #blah blah blah, what is your name?
    while(Classes.hero.name == ""):
        Classes.hero.name = raw_input()   
        Classes.hero.name = Classes.hero.name.title()

def chooseWeapon(object1):
    valid = False
    #blah blah blah, what weapon you want?
    
    print ("1: " + Classes.sword.name + " " + Classes.sword.desc + "\n")
    print ("2: " + Classes.spear.name + " " + Classes.spear.desc + "\n")
    print ("3: " + Classes.axe.name + " " + Classes.axe.desc + "\n")

    while(valid == False):
        choice = raw_input()
        choice = choice.lower()
        if choice == 1 or choice == "one" or choice == "sword":
            Classes.hero.equipment = Classes.sword
            valid = True
        elif choice == 2 or choice == "two" or choice == "spear":
            Classes.hero.equipment = Classes.spear
            valid = True
        elif choice == 3 or choice == "three" or choice == "axe":
            Classes.hero.equipment = Classes.axe
            valid = True

         
        
