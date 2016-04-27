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
    attack = ((object1.attack + object1.weapon.attack) +            #Base number
             randint((-object1.attack + (int(.5 * object1.attack))),#random bottom range
             (object1.attack + (int(.5 * object1.attack)))))        #random upper range
    #Determine defense number
    defense = ((object2.defense + object2.weapon.defense) +         #Base number  
              randint(0,                                            #set bottom range
              (object2.defense + (int(.5 * object2.defense)))))     #random upper range

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

#The third object is the spell
def spellCalc(object1, object2, object3):
    #Ensure damage is cleared to 0.
    damage = 0
    
    #Determine attack number
    attack = ((object1.attack + spell.attack) +                     #Base number
             randint((-object1.attack + (int(.5 * object1.attack))),#random bottom range
             (object1.attack + (int(.5 * object1.attack)))))        #random upper range
    #Determine defense number
    defense = ((object2.defense + object2.weapon.defense) +         #Base number  
              randint(0,                                            #set bottom range
              (object2.defense + (int(.5 * object2.defense)))))     #random upper range

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
    object2.currentHP -= attackCalc(object1, object2)
    if object2.currentHP <= 0 :
        print (object2.name + " has died...You goddamn murderer!!!")
    else:
        print(object2.name + " has " + str(object2.currentHP) + " HP left!\n")

def battleSpell(object1, object2):
    print("Now it's " + object1.name +"'s turn!")
    #Run the attack calculator, and subject the damage from the object's HP
    object2.currentHP -= attackCalc(object1, object2)
    if object2.currentHP <= 0 :
        print (object2.name + " has died...You goddamn murderer!!!")
    else:
        print(object2.name + " has " + str(object2.currentHP) + " HP left!\n")
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
    while(object1.currentHP > 0 and object2.currentHP > 0):
        battle(object1, object2)
        if object2.currentHP > 0:
            battle(object2, object1)
    object1.currentHP = object1.maxHP
    object2.currentHP = object1.maxHP

def start(object1):
    #Include your print statements for opening narrative
    
    
    getName(object1)

    #blah blah blah, welcome hero, now choose your weapon
    
#Get the user's name, or hero's name if they don't use their own.
def getName():
    #blah blah blah, what is your name?
    while(Classes.hero.name == ""):
        Classes.hero.name = input()   
        Classes.hero.name = Classes.hero.name.title()

#Allow user to choose a weapon
def chooseWeapon():
    valid = False
    #blah blah blah, what weapon you want?
    
    print ("1: " + Classes.sword.name + " " + Classes.sword.desc + "\n")
    print ("2: " + Classes.spear.name + " " + Classes.spear.desc + "\n")
    print ("3: " + Classes.axe.name + " " + Classes.axe.desc + "\n")

#Make sure the user enters a valid input.
    while(valid == False):
        choice = input()
        choice = choice.lower()
        if choice == "1" or choice == "one" or choice == "sword":
            Classes.hero.weapon = Classes.sword
            valid = True
        elif choice == "2" or choice == "two" or choice == "spear":
            Classes.hero.weapon = Classes.spear
            valid = True
        elif choice == "3" or choice == "three" or choice == "axe":
            Classes.hero.weapon = Classes.axe
            valid = True
        else:
            print ("\nChoice was invalid, try again...\n")
    print("You picked up the " + Classes.hero.weapon.name + "!!!")

#function to play when the user dies
def gameOver():
    print ("\n\t\"I tried!!!\" you plead, but the stiff, expressionless\n \
            figure of the Reaper doesn't change.  It continues to \n \
            drag you to a small boat on the edge of what you assume \n \
            to be the river Styx.  It's a shame that the world you're \n \
            leaving will never know your name or your deeds.\n")
    
#Determine if the user wants to play again, 
def playAgain():
       
    print ("Would you like to play again? (yes/no)\n")
    yesNo = input()
    yesNo = yesNo.lower()
    if yesNo == "yes" or yesNo == "y":
        return True
    else:
        return False
#This will be the simple menu for the user to choose.
def heroAction(object1, object2):
    print ("\nIt is your turn, how wil you proceed?\n")
    print ("1 = Attack\n"
           "2 = Spells\n")
    #get input
    action = input()
    action = action.lower()
    
    if(action == "1" or action == "one" or action == "attack"):
        runBattle(object1,object2)
    
    elif(action == "2" or action == "two" or action == "spells"):
        print("What spell do you wish to use?\n")
        print ("1: " + Classes.lightningBolt.name + " - Number of uses left: " + str(Classes.lightningBolt.uses) + "\n"
               "2: " + Classes.fireBall.name + " - Number of uses left: " + str(Classes.fireBall.uses) + "\n"
               "3: " + Classes.heal.name + " - Number of uses left: " + str(Classes.heal.uses) + "\n"
               "4: Back to main menu\n" )




    
'''
***Riddles***
'''

def firstRiddleHallway():
    print ("Which Hallway do you go down? Left, Middle, or Right?")
    valid = False
    while (valid == False):
        choice = input()
        choice = choice.lower()
        if choice == "left":
                print ("Moving forward, you become dizzy with fear, and all light is extinguished, but before you can even think to turn back, it's too late!"
                        "\nYou feel the ground dissapear underneath your feet as you fall to your death!"
                        "\n...Today was indeed your last breath.")
                valid = True
                endGame = True
                gameOver()
                return endGame
        elif choice == "middle":
                print ("Moving forward, you become dizzy with fear, and darkness surrounds you."
                   "\nYou make out a small flame ahead...and...is that growling you hear?"
                   "\nYou take a few more steps forward, and before you are able to think otherwise,"
                   "\nyou see the source of those growls..."
                   "\nA huge wolf!!!!!"
                   "\nYou dodge it's initial lunge, but not before catching it's name on it's collar"
                   "\n...Kujo..."
                   "\nYou steady your weapon as Kujo, gets ready to lunge again, clearly this wolf wants nothing more than to eat your face off.")
                valid = True
                
            #wolf1 function?
        elif choice == "right":
                print ("Moving forward, you become dizzy with fear, and darkness surrounds you."
                   "\nYou make out a small flame ahead...and...is that growling you hear?"
                   "\nYou take a few more steps forward, and before you are able to think otherwise,"
                   "\nyou see the source of those growls..."
                   "\nA...tiny puppy????"
                   "\nYou dodge it's initial lunge, but not before catching it's name on it's collar"
                   "\n...Fluffy..."
                   "\nYou steady your weapon as Fluffy, gets ready to lunge again, clearly this puppy wants nothing more than to lick your face."
                   "\nRight?")
                valid = True
                
            #wolf2 function?
        else:
                print ("You must pick one, there is no turning back.  Left Middle or Right?")


def secondRiddleBoss():
    print ("How do you procede? with Rage, Precision, or Confidence?")
    valid = False
    while (valid == False):
        choice = input()
        choice = choice.lower()
        if choice == "rage":
                print ("Furious with your situation, you want nothing more than to destroy your opponent."
                       "\nTo rip him apart and see him wither in pain and anguish"
                       "\nand watch as he chokes on his arrogance!!!  You will not be happy until your weapon is soaked in it's blood!!!")
                valid = True
                #bossMagic battle function
        elif choice == "precision":
                print ("This is it, it's time to take on that arrogant voice!"
                       "\nYou ready your weapon and take caution."
                       "\nChances are you are about to take on a formidable foe!"
                       "\nWith a deep breath, you focus and approach slowly, ready for anything!")
                valid = True
                #bossAxe battle function
        elif choice == "confidence":
                print ("HA! What a joke!"
                       "\nThere is nothing that can stop you now!!!"
                       "\nThis shouldn't take more than a minute.")
                valid = True
                #bossMagicAxe function
        else:
                print ("You must finish this fight, there is no turning back.  approach with Rage, Precision, or Confidence?")

           
        
