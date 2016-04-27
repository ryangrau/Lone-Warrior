'''
***Class Definitions***
'''

class entity:
        def __init__(self, name, currentHP, maxHP, attack, defense, weapon):
                self.name = name
                self.currentHP = currentHP
                self.maxHP = maxHP
                self.attack = attack
                self.defense = defense
                self.weapon = weapon

        def debugInfo(self):
            print (self.name)
            print (self.currentHP)
            print (self.maxHP)
            print (self.attack)
            print (self.defense)
            print (self.weapon)

class weapon:
    def __init__(self, name, attack, defense, desc):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.desc = desc

    def debugInfo(self):
        print (self.name)
        print (self.attack)
        print (self.defense)
        print (self.desc)

    
#Class for creating spells.  I'll just make a simple list.
class spell:
    def __init__(self, name, attack, effect, currentUse, maxUse, desc):
        self.name = name
        self.attack = attack
        self.effect = effect
        self.currentUse = currentUse
        self.maxUse = maxUse
        self.desc = desc

    def debugInfo(self):
        print ("Name is " + self.name)
        print ("Attack value is " + str(self.attack) +
               " & My effect is " + str(self.effect))
        print ("Description: " + self.desc)
        ''' 
        def onEffect(self.effect):
            if self.effect == True:   #Any value in effect will evalute to true, only 0 is false
        '''
'''
 I decided to pull out the effect mechanic in interest of time.  Perhaps I'll implement it later just to do it.
 I'd need to make a duration and turn count with the battles.  Not bad, but still, time.
        
#These will be the effects for the spell class listed above.  It will need
#to know the stat that it needs to modify.  Ex.  Blind will affect attack with -2
class effect:
    def __init__(self, name, stat, mod, duration):
        self.name = name
        self.stat = stat
        self.mod = mod
        self.duration = duration

    def debugInfo(self):
        print ("Name is " + self.name)
        print ("The stat I modify is  " + str(self.stat) +
               " & the mod value is  " + str(self.mod))
        
'''
'''
So I know that class looks different than the way I showed you, but it's
actually easier to use.  Rather than initiating every value line by line,
we can do this for a "Sword, with and attack of +3 and defense of +1"
'''

'''
***Object Creation***
'''

#These are the 3 generic weapons I've made.  Feel free to add some.
#It uses the "weapon" class
sword = weapon("Sword",2,1,"A modest blade featuring a bland " +
                            "crossguard. The smithy clearly had the edge " +
                            "in mind when designing this blade.")
spear = weapon("Spear",1,2, "A wooden shaft with a crudely fastened blade ," +
                            "atop of it.  Might work as an offensive weapon, " +
                            "but I could make defensive use of it's range")
axe = weapon("Axe",3,0, "A masterfully designed weapon, complete with a " +
                         "damascus weaving in the steel and fluting rimming the edge. " +
                         "Shame it has little to no defensive worth.")
none = weapon("Nothing",0,0,"")


hero = entity("",100,100,18,10,sword)
wolf1 = entity("Kujo",100,100,20,10,none)
wolf2 = entity("Fluffy",100,100,26,8,none)
bossMagic = entity("Yomahmah",100,100,30,12,none)
bossAxe = entity("Axesaw Duggin",100,100,38,6,none)
bossMagicAxe = entity("Mahess",100,100,100,100,none)


#These are 3 spells I've made.  Again, feel free to add some.
#1 is pure damage, the other 2 are status effect spells
lightningBolt = spell("Lightning Bolt",30,"", 1,1,
                      "Generic Lightning Bolt description - 'Zap'")
fireBall = spell("Fire Ball",30,"", 1,1,
                 "Your run-of-the-mill propelled ball of pure fire.  Still fun though.")
heal = spell("Heal",-25,"", 2, 2, 
             "Hey, it's better than waiting for the wounds to close up")
#blind = spell("Blind",0,"atkDown", "Sometimes a best defense is crippling your opponents offense.")  Taken out
#shatter = spell("Shatter",0,"defDown", "Armor and shields are useless when they're in pieces.")   Taken out
#regen = spell("Regenerate",0,"mend", "Slowly mend your wounds over time.")  Taken out

#These define the status effects.  Simple, one affects attack, one affects defense.
#Eventually, when we have the entity class, we'll change "attack" and "defense" to entity.attack and entity.defense
#atkdown = effect("atkDown", "attack", -5,4)
#defDown = effect("defDown", "defense", -5,4)
#mend = effect("mend", "currentHP", +5,6)

