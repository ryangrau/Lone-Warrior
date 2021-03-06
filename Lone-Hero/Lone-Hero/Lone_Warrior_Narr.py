import Functions
import Classes

from time import sleep

'''
***opening narrative
'''
SLEEP_TIMER = 5


def openNarr():
    print ("Well well well.  It looks like you've fallen into my dungeon!" 
           "\nYou are probably asking yourself, who's voice am I hearing right now?" 
           "\nLet me cut to the chase.  I'm the guy who is going to slaughter you!" 
           "\nWhat is your name? I want to remember what to call you as I munch on your bones!"
           "\n (Please enter your name)")
    Functions.getName()

    print ("\nWell " + Classes.hero.name +
            "\n...You see there is only one way out of this dungeon"
            "\nand it's through me."
            "\n...Actually there are a few other ways out but trust me,"
            "\nthe results are the same."
            "\nMUAHAHAHAHA.")
    sleep(SLEEP_TIMER)
    print ("\nI'm sure you are also curious as to how I know you're"
           "\neven here, or where exactly you are."
           "\nI can smell your fear, and your vile human odor..."
           "\nIt disgusts me."
           "\nSo for the sake of my sense of smell, let's make this quick."
           "\n...Move vermin! Come meet your end you pathetic filth!"
           "\nCome breathe your last breath!!!\n")
    sleep(SLEEP_TIMER)

'''
***picking a weapon narrative
'''

def pickWeaponNarr():
    print ("After checking yourself for any injuries during the stumble,"
           "\nyou gather up your gusto."
           "\nYou look behind you and it's obvious there is no climbing out of here."
           "\nLooks like forward is the only direction you can go.\n")
    sleep(SLEEP_TIMER)
    print ("\nAs you look ahead, you see something glimmer in the fading light."
           "\nYou walk forward, pick it up and dust it off."
           "\nLooks like you've found a variety of weapons..."
           "\nWhich one do you pick?\n") #player picks a weapon
    Functions.chooseWeapon()
    print ("\nYou already know just how important this will be in the upcoming journey.")


'''
***riddles***
'''

def firstRiddleNarr():
    print ("Thinking on your situation you become"
           "\nangered by the arrogance of the voice filling the dark halls of the dungeon."
           "\nYou carefully tread forward, nevertheless."
           "\nBut your anger wavers. Your fear starts to overcome your confidence..."
           "\nMaybe this will be the day you breathe your last breath..."
           "\nAs your hands go numb, your body cold with fear, you come across a "
           "\nfaded plaquerd nailed to a wooden stake in the ground."
           "\nIt's barely legible but in the dim glow you're able to read:\n")
    sleep(SLEEP_TIMER)
#first riddle
    print ("THERE ARE BUT THREE OPTIONS TO CHOOSE"
            "\nONE TO MAKE YOU LOSE" #left which is the pit
            "\nTWO TO MAKE YOU TRY" #middle which is Kujo
            "\nANY OF WHICH CAN SEE YOU DIE" #right which is Fluffy
            "\nYou stare up over the plaquard and see there are three different hallways "
            "\nyou can go down...but which one?\n")
#player is then prompted with, "Left, Middle, or Right?" 
    object2 = Functions.firstRiddleHallway()
    return object2

def secondRiddleNarr():
    print ("Well, well, well.  I can smell the blood of your opponent on your" 
            "\ngrimey putrid human hands."
            "\nLooks like you've bested my pet"
            "\nI'd say I'm impressed...but I'm not.  I'm only more angered that " 
            "\nI have to go on smelling such horrifying odors."
            "\nWell warrior, if you find yourself so brave, come on then..."
            "\nmy hatred for you is only going to make me stronger."
            \
            "\n..."
            )
    sleep(SLEEP_TIMER)
    print("\nYou look down at your bloodied armor, fear has left you entirely."
            "\nThis battle has only empowered you!"
            "\nThe arrogant voice has called you out, and now, after destroying your opponent you are ready!"
            "\nYou recall all your confidence as a deadly warrior, and become enraged with bloodlust."
            "\nThis...will...NOT...be...your...last...breath!!!!"
            "\nIn full blown sprint you are only stopped by another plaquard, "
            "\nit's golden scripts catching your eye - the shimmering words read:")
#second riddle
    sleep(SLEEP_TIMER)
    print ("YOU'VE COME A LONG WAY"
            "\nTHAT'S RARE TO SEE I MUST SAY"
            "\nNO CHEERING TO BE HAD YET"
            "\nTHERE IS STILL A FOE TO BE MET"
            "\n...WILL YOU BURN LIKE FIRE IN THE NIGHT?" #bossMagic. Has high damage output, but less HP.
            "\n...SLICE THROUGH FEAR WITH FIERCE MIGHT?" #bossAxe. Has highest damage output, but least HP.
            "\n...OR PERHAPS, THIS WHOLE TIME, YOU HAVEN'T BEEN RIGHT?") #bossMagicAxe. God-Mode.  Super high DPS, very high HP.
#player is prompted once again, "How do you approach? With rage, precision, or confidence?" rage = bossMagic; precision = bossAxe; confidence = bossMagicAxe
    object2 = Functions.secondRiddleBoss()
    return object2



'''
***after first fight narrative
'''

def riddleHeal():
    print ("The growling should have been warning enough."
           "\nBut to say that battle was easy would be a lie."
           "\nLuckily you never travel without a healing potion."
           "\nYou take a full swig and immedietely feel it's effects."
           "\nAfter a deep breath you feel great and your wounds are gone!")
    Classes.hero.resetHP()

'''
***losing to the boss
'''

def loseBoss():
    print ("\nYou feel the searing pain spread throughout your "
           "\nbody as you fall limp to the ground. "
           "\nYou struggle, plead with yourself to keep going."
           "\nThe blood is filling up your lungs as you choke, "
           "\nbroken bones start protruding through your hacked up body."
           "\n...you know what this is, as much as you wish you could deny..."
           "\nthis unholy place is where you die."
           "\nDeath looms over you...as you breathe...your...last...breath.")
    


'''
***beating the boss
'''

def winBoss():
    print ("\nBreathing heavy you look forward. There is light, beautiful shining light that beckons you!"
            "\nYou look down at the disgusting bloodied body of your foe."
            "\nYou raise your weapon high, letting the blood drip off for a few seconds, "
            "\nbefore slamming it back down into the monsters face!"
            "\nYou step on and over it's putrid body, and start to walk off towards the light..."
            "\nYou take one last look back at what you've overcome and think to yourself..."
            "\n'looks like I'm the one still breathing after all'.")
