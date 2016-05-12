'''
***Class Definitions***
'''

entityList=[]
spellList=[]


class entity:
        def __init__(self, name, currentHP, maxHP, attack, defense, weapon):
                self.name = name
                self.currentHP = currentHP
                self.maxHP = maxHP
                self.attack = attack
                self.defense = defense
                self.weapon = weapon
                entityList.append(self)

        def __iter__(self):
            for i in entity:
                print(name)

        def debugInfo(self):
            print (self.name)
            print (self.currentHP)
            print (self.maxHP)
            print (self.attack)
            print (self.defense)
            print (self.weapon)

        def resetHP (self):
            self.currentHP = self.maxHP

        def loopName(self):
            for i in self.name:
                print (self.name)

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
        spellList.append(self)

    def debugInfo(self):
        print ("Name is " + self.name)
        print ("Attack value is " + str(self.attack) +
               " & My effect is " + str(self.effect))
        print ("Description: " + self.desc)
        print ("My current Uses are " + str(self.currentUse) +
               "and my max Uses are " + str(self.maxUse))

    def resetUses(self):
        self.currentUse = self.maxUse
        ''' 
        def onEffect(self.effect):
            if self.effect == True:   #Any value in effect will evalute to true, only 0 is false
        '''

'''
***Object Creation***
'''

#These are the 3 generic weapons I've made.  Feel free to add some.
#It uses the "weapon" class
sword = weapon("Sword",2,1,"A modest blade featuring a bland crossguard.\n" 
                            "The smithy clearly had the edge in mind when designing this blade.")
spear = weapon("Spear",1,2, "A wooden shaft with a crudely fastened blade atop of it.\n"
                            "Might work as an offensive weapon but I could make defensive use of it's range")
axe = weapon("Axe",3,0, "A masterfully designed weapon, complete with a damascus weaving\n"
             "in the steel. Shame it has little to no defensive worth.")
none = weapon("Nothing",0,0,"")


hero = entity("",50,100,18,10,none)
wolf1 = entity("Kujo",100,100,10,10,none)
wolf2 = entity("Fluffy",100,100,16,8,none)
bossMagic = entity("Yomahmah",100,100,30,12,none)
bossAxe = entity("Axesaw Duggin",100,100,38,6,none)
bossMagicAxe = entity("Mahess",100,100,100,100,none)


#These are 3 spells I've made.  Again, feel free to add some.
lightningBolt = spell("Lightning Bolt",40,"", 1,1,
                      "Generic Lightning Bolt description - 'Zap'")
fireBall = spell("Fire Ball",40,"", 1,1,
                 "Your run-of-the-mill propelled ball of pure fire.  Still fun though.")
heal = spell("Heal",-25,"", 2, 2, 
             "Hey, it's better than waiting for the wounds to close up")


