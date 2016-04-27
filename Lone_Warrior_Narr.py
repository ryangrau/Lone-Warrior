import Functions
import Classes

'''
***
'''

def openNarr():
    print ("Well well well.  It looks like you've fallen into my dungeon!"
            "\nYou are probably asking yourself, who's voice am I hearing right now?"
            "\nLet me cut to the chase.  I'm the guy who is going to slaughter you!"
            "\nWhat is your name? I want to remember what to call you as I munch on your bones!"
#player would enter their name
            "\n (Please enter your name)")
    Functions.getName()
    print ("\nWell " + Classes.hero.name +
            "\n...You see there is only one way out of this dungeon and it's through me."
            "\n...Actually there are a few other ways out but trust me, the results are the same."
            "\nMUAHAHAHAHA."
            "\nI'm sure you are also curious as to how I know you're even here, or where exactly you are."
            "\nI can smell your fear, and your vile human odor...It disgusts me."
            "\nSo for the sake of my sense of smell, let's make this quick."
            "\n...Move vermin! Come meet your end you pathetic filth! Come breathe your last breath!!!")

'''
***
'''

def pickWeaponNarr():
    print ("After checking yourself for any injuries during the stumble, you gather up your gusto."
           "\nYou look behind you and it's obvious there is no climbing out of here."
           "\nLooks like forward is the only direction you can go."
           "\nAs you look ahead, you see something glimmer in the fading light."
           "\nYou walk forward, pick it up and dust it off."
           "\nLooks like you've found..." #player picks a weapon
    Functions.chooseWeapon() + "!!!"
    print ("\nYou already know just how important this will be in the upcoming journey."


'''
***riddles***
'''

def firstRiddleNarr():
    print ("Thinking on your situation you become"
           "\nangered by the arrogance of the voice filling the dark halls of the dungeon."
           "\nYou carefully tread forward, nevertheless."
           "\nBut your anger wavers. Your fear starts to overcome your confidence..."
           "\nMaybe this will be the day you breathe your last breath..."
           "\nAs your hands go numb, your body cold with fear, you come across a faded plaquerd nailed to a wooden stake in the ground."
           "\nIt's barely legible but in the dim glow you're able to read:")
#first riddle
    print ("THERE ARE BUT THREE OPTIONS TO CHOOSE"
        "\nONE TO MAKE YOU LOSE" #A - the letters won't be visible to the player until prompted for an answer.  'A' is the PIT
        "\nTWO TO MAKE YOU TRY" #B 'B' is the hard wolf.
        "\nANY OF WHICH CAN SEE YOU DIE" #C 'C' is the easy wolf.
        "\nYou stare up over the plaquard and see there are three different hallways you can go down...but which one?")
#player is then prompted with, "Left, Middle, or Right?" Left is 'A', Middle is 'B', and Right is 'C'.




def secondRiddleNarr():
    print ("YOU'VE COME A LONG WAY"
        "\nTHAT'S RARE TO SEE I MUST SAY"
        "\nNO CHEERING TO BE HAD YET"
        "\nTHERE IS STILL A FOE TO BE MET"
        "\n...WILL YOU BURN LIKE FIRE IN THE NIGHT?" #A = boss that uses magic. Has high damage output, but less HP.
        "\n...SLICE THROUGH FEAR WITH FIERCE MIGHT?" #B = boss that uses axe. Has highest damage output, but least HP.
        "\n...OR PERHAPS, THIS WHOLE TIME, YOU HAVEN'T BEEN RIGHT?") #C = boss that uses magic axe. God-Mode.  Super high DPS, very high HP.

#player is prompted once again, "How do you approach? With Rage, Precision, or Confidence?"
#Rage is 'A', Precision is 'B', and Confidence is 'C'.




