import Classes
import Functions
import Lone_Warrior_Narr

#This will house the flow of our program.  We'll invoke functions and classes
#from the files we're importing.  The goal is for more readable code.

#Here's an example of how we'd call the functions/classes in the other files

#while playAgain = true, play it again!
#Global Variables are cheating, we should get rid of these.
#I.E. get more creative in incorporating them as control statements
#If this were C++, we could just do a "do-while" loop.

again = True


while(again):
    #Reset notDead value to True, and resetsHP for all entities.
    notDead = Functions.setupGame()

    
    #Run opening narrative, collect name
    Lone_Warrior_Narr.openNarr()
    
    #Allow hero to pick a weapon
    Lone_Warrior_Narr.pickWeaponNarr()
    
    #Run narrative and the first riddle.  Riddle determines who the hero fights
    #(or if the hero instantly dies)
    #The chosen opponent gets stored in object2, to be later passed into the battle function
    object2 = Lone_Warrior_Narr.firstRiddleNarr()
    
    #See if hero suffered insta-death
    notDead = Functions.isHeroDead(Classes.hero)
    
    #If not dead, go on to the fight!
    if(notDead):
        print(object2.name)
        Functions.runBattle(Classes.hero, object2)
        
        #Is the hero dead now?
        notDead = Functions.isHeroDead(Classes.hero)
        if(notDead):
            #Heal player
            Lone_Warrior_Narr.riddleHeal()
      
            #Second riddle to determine boss
            object2 = Lone_Warrior_Narr.secondRiddleNarr()
            Functions.runBattle(Classes.hero, object2)

            #Did the hero survive?
            notDead = Functions.isHeroDead(Classes.hero)    
            if(notDead):
                Lone_Warrior_Narr.winBoss()
            else:
                Lone_Warrior_Narr.loseBoss()

    #Any deaths will fail the if statements, and land in this function.
    if(notDead == False):
        Functions.gameOver()

    again = Functions.playAgain()
    