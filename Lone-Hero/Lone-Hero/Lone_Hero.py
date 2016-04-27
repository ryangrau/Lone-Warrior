import Classes
import Functions
import Lone_Warrior_Narr

#This will house the flow of our program.  We'll invoke functions and classes
#from the files we're importing.  The goal is for more readable code.

#Here's an example of how we'd call the functions/classes in the other files
'''
#while playAgain = true, play it again!
again = True
endGame = False
while(again):

    Lone_Warrior_Narr.openNarr()
    endGame = Functions.firstRiddleHallway()
    #print (endGame)  Just debugging purpose
    if (endGame != True):
        Lone_Warrior_Narr.secondRiddleNarr()




    #Functions.runBattle(Classes.wolf1, Classes.wolf2)


    again = Functions.playAgain()
#Lone_Warrior_Narr.openNarr()
'''

Functions.heroAction(Classes.hero, Classes.wolf1)

