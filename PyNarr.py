

print ("Well well well.  It looks like you've fallen into my dungeon! \nYou are probably asking yourself, who's voice am I hearing right now?"
        "Let me cut to the chase.  I'm the guy who is going to slaughter you! \nYou see there is only one way out of this dungeon and it's through me."
        "...Actually there are a few other ways out but trust me, the results are the same.\nMUAHAHAHAHA."
        "I'm sure you are also curious as to how I know you're even here, or where exactly you are.\nI can smell your fear, and your vile, rank human odor...It disgusts me."
        "\nSo for the sake of my sense of smell, let's make this quick.\n...Move vermin! Come meet your end you pathetic filth! Come breathe your last breath!!!")

#Player is prompted, would you like to play? (y/n):
#Assuming they say yes, they are met with a little more narrative.


print ("Angered by the arrogance of the voice filling the dark halls of the dungeon you carefully tread forward."
        "\nYour fear starts to overcome your confidence...maybe this will be the day you breathe your last breath..."
        "\nAs your hands go numb, your body cold with fear, you come across a faded plaquerd nailed to a wooden stake in the ground."
        "\nIt's barely legible but in the dim glow you're able to read:")


#riddle1
print ("THERE ARE BUT THREE OPTIONS TO CHOOSE"
        "\nONE TO MAKE YOU LOSE" #A - the letters won't be visible to the player until prompted for an answer.  'A' is the PIT
        "\nTWO TO MAKE YOU TRY" #B 'B' is the hard wolf.
        "\nANY OF WHICH CAN SEE YOU DIE" #C 'C' is the easy wolf.
        "\nYou stare up over the plaquard and see there are three different hallways you can go down...but which one?")
#player is then prompted with, "Left Hallway, Middle Hallway, or Right Hallway?" Left is 'A', Middle is 'B', and Right is 'C'.

#based off of whatever happens with the players option there will be 'Fight-based' narrative, very basic.

#if they choose the pit:
print ("You become dizzy with fear, and all light is extinguished, but before you can even think to turn back, it's too late!"
        "\nYou feel the ground dissapear underneath your feet as you fall to your death!"
        "\n...Today was indeed your last breath.")
#You've fallen into a deadly pit player! Would you like to play again? (y/n)


#Let's assume the player picks a battle option and wins the fight - continuing the narrative:

print ("Well, well, well.  It looks like I can smell the blood of your opponent on your grimey putrid human hands."
        "\nI'd say I'm impressed...but I'm not.  I'm only more angered that I have to go on smelling such horrifying odors."
        "\nWell warrior, if you find yourself so brave, come on then...my hatred for you is only going to make me stronger."
        "\n..."
        "\nYou look down at your bloodied armor, fear has left you entirely."
        "\nThis battle has only empowered you!"
        "\nThe arrogant voice has called you out, and now, after destroying your opponent you are ready!"
        "\nYou recall all your confidence as a deadly warrior, and become enraged with bloodlust."
        "\nThis...will...NOT...be...your...last...breath!!!!"
        "\nIn full blown sprint you are only stopped by another plaquard, it's golden scripts catching your eye - the shimmering words read:")

print ("YOU'VE COME A LONG WAY"
        "\nTHAT'S RARE TO SEE I MUST SAY"
        "\nNO CHEERING TO BE HAD YET"
        "\nTHERE IS STILL A FOE TO BE MET"
        "\n...WILL YOU BURN LIKE FIRE IN THE NIGHT?" #A = boss that uses magic. Has high damage output, but less HP.
        "\n...SLICE THROUGH FEAR WITH FIERCE MIGHT?" #B = boss that uses axe. Has highest damage output, but least HP.
        "\n...OR PERHAPS, THIS WHOLE TIME, YOU HAVEN'T BEEN RIGHT?") #C = boss that uses magic axe. God-Mode.  Super high DPS, very high HP.

#player is prompted once again, "How do you approach? With Rage, Precision, or Confidence?"
#Rage is 'A', Precision is 'B', and Confidence is 'C'.

#Fight-based narrative text takes place during fight.
#Assuming player loses fight:
print ("\nYou feel the searing pain spread throughout your body as you fall limp to the ground.  You struggle, plead with yourself to keep going."
        "\nThe blood is filling up your lungs as you choke, broken bones start protruding through your hacked up body."
        "\n...you know what this is, as much as you wish you could deny...this unholy place is where you die."
        "\nDeath looms over you...as you breathe...your...last...breath.")
#You got far player, but not far enough. Want to try again? (y/n)

#Assuming player wins fight:
print ("\nBreating heavy you look forward. There is light, beautiful shining light that beckons you!"
        "\nYou look down at the disgusting bloodied body of your foe."
        "\nYou raise your weapon high, letting the blood drip off for a few seconds, before slamming it back down into the monsters face!"
        "\nYou step on and over it's putrid body, and start to walk off towards the light..."
        "\nYou take one last look back at what you've overcome and think to yourself...'looks like I'm the one still breathing after all'.")
#print something like, You've beaten the boss!!! Congratulations player!! Here is your score ____!!!\n
#Now go tell all your friends how much better at this game you are than them!!\n
#Hey! any chance you're feeling froggy? Enough to play again? (y/n)
