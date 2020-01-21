###########1111
class Dog():
    age = 0 
    name = ""
    weight = 0
dog =Dog()
dog.age = 1
dog.name = "jgnb"
dog.weight = 24


##22222222222222222
class Person():
    name = ""
    cellPhone = ""
    email = ""
p = Person()
p.name = "kj["
p.cellPhone = "kdb"
p.email = "bjrgt"
    
###########33333333333333333333    
class Bird():
    color = ""
    name  =""
    breed = ""
myBird = Bird()
myBird.color = "green"
myBird.name = "Sunny"
myBird.breed = "Sun Conure"

#######################44444444444444444444
class player:
    name = ""
    strength = 0
    coordinates = 0,0
p = player()
p.name = "Hitler"
p.strength = 99
p.coordinates = 1939, 1945

###################5555555555555555555
class Person():
    name = ""
    money = ""# money = 0
nancy = Person() 
name = "" #nancy.name = ""
money = 100 #nancy.money = 100

####################66666666666
class Person():
    name = "Bob"
    money = 0
bob = Person()
print(bob.name, "has", bob.money, "dollars")
    


####################
#########OOP4######
##################
##########11111111111
import time
import random
class Cat():
    name = ""
    color = ""
    weight = 0
    def meow(self):
        for i in range (15):
            time.sleep(random.randint(1,15))    
            print("Meow")
c = Cat()
c.color = "green"
c.name = "govno"
c.weight = 80              
c.meow()   

##########222222           
            
class aadress():
    strn = "Grow"
    hnum= 5
    def pr(self):
        print('You are on {0} Street, {1}'.format(self.strn, self.hnum))
a = aadress()
a.pr()
              

################33333333333333333
class monster():
    hp = 100
    name = 'Mari'
    def decreasehp(self):
        amount = 10
        while self.hp > 0:
            self.hp -= amount
            print('Monster {0} is still alive\n{1} HP left'.format(self.name, self.hp))
            time.sleep(1)
        if self.hp == 0:
            print('Monster has been killed!')
            time.sleep(0.5)
            print('You WOOOOOOOOON')
m = monster()
m.decreasehp()

###########warrior
import time
''' Creating main class'''
class warrior():
   hp1=hp2 = 100   
   dam = 20
   def cl(self):        
        a = 0
        while self.hp1 and self.hp2 > 0:
            '''while to count getting damage'''
            r = random.randint(1,2)          
            time.sleep(1)
            a += 1
            if r == 1:
                self.hp1 -= self.dam
                print('Player 2 hits PLayer 1')
                print('Player 1 loses {0} HP \nalready lost {1} HP \n {2} HP left \n {3}'.format(self.dam, ((self.dam) * a), (100 - ((self.dam) * a)), ('-')*10))
            else:
                self.hp2 -= self.dam
                print('Player 1 hits PLayer 2')
                print('Player 2 loses {0} HP \nalready lost {1} HP \n {2} HP left \n {3}'.format(self.dam, ((self.dam) * a), (100 - ((self.dam) * a)), ('-')*10))
            
            time.sleep(1)
            '''ending '''
            if self.hp1 == 0:
                print('Player 1 is dead! \n Player 2 wins')
            elif self.hp2 == 0:
                print('Player 2 is dead! \n Player 1 wins')
          

            
           
w = warrior()
w.cl()




####################game

import random
''' Create class and call it one to use it as the parent class '''
class one:
    '''generator with every soldier number and soldier's command'''
    def __init__(self, num, commandid):
        self.num = num
        self.commandId = commandid
        ''' Another generator'''
class hero(one): 
    def __init__(self,  num, commandid, name, lvl=1):
        one.__init__(self, num, commandid)
        self.name = name
        self.lvl = lvl

    def getlevel(self):
        return self.lvl



    def inclvl(self): 
        
        ''' Increase lvl if command contains more soldiers'''
        
        self.lvl += 1
        print('Уровень героя', self.name,'увеличен на 1 и равен', self.lvl)
        
class sol(one):
    ''' class and functiion to make soldier follow hero1'''
    def gotohero(self, Hero):
        print('Солдат ', self.num, 'следует за героем', Hero.name, 'с номером', Hero.num)
H1 = hero(1, 1, '1')
H2 = hero(2, 2, '2')
armyH1, armyH2 = [], []

for i in range(3, 10):
    '''Adding soldiers to teams randomly '''
    n = random.randint(0, 1)
    if n:
        armyH1.append(sol(i, 1))
        print('Солдат с номером', i, 'добавлен в армию', H1.name)
    else:
        armyH2.append(sol(i, 2))
        print('Солдат с номером', i, 'добавлен в армию', H2.name)

print('Армия героя', H1.name, ' - ', len(armyH1))
print('Армия героя', H2.name, ' - ', len(armyH2))

if len(armyH1) > len(armyH2):
    print('В армии', H1.name, 'больше солдат - увеличиваем его уровень')
    '''Condition to increase hero lvl'''
    H1.inclvl()
else:
    print('В армии', H2.name, 'больше солдат - увеличиваем его уровень')
    H2.inclvl()
armyH1[1].gotohero(H2)        
        
    

        
              
              
              
              
              
