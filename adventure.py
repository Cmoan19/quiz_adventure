# An adventure game
health = 20
attack = 0
defense = 0
magic = 0
ogreHp = 20
IogreHp = 20
Iogre2Hp = 20
Shrek = 50


from random import randint

def startingroom():
    global health, attack, defense, magic

    print("you find a chest!")
    chest = input ("Do you open the chest? ")

    if chest.upper()[0] == "Y":
        print("You found a rusty sword, a pie and a leather tunic")
        attack = 10
        defense = 5
        
    print("You move on")
    room2()
    
    
          

    

def room2():
    global health, attack, defense, magic

    fall = randint(0, 1)

    if fall == 0:
        print(" ")
        print("You fell and found yourself in a swamp-like area.")
        print("You see a small shack hidden under a mount")
        shack = input ("Do you enter? ")

        if shack.upper()[0] == "Y":
            print("Inside you find a battle axe, onions and chainmail boots")
            attack = 30
            defense = 15
        room4()
    
    elif fall == 1:
        room3()
    

        
 
def room3():
    global health, attack, defense, magic

    print(" ")
    print("You go through the door and find a book on a pedel stool.")
    print("You decide to read it.")
    print("You read the book and learn the ability to shoot fire")
    magic = 2

    room5()
    

    



def room4():
    global health, attack, defense, magic

    print(" ")
    print("After leaving the swamp you find youself in a forest.")
    print("As you walk along an ogre jumps out and attacks you.")
    fight = input ("What do you do? Chose you wepon. Axe. ")

    if fight.upper()[0] == "A":
        print("You swipe at the ogre")
        ogreHp = 0
        print("ogre health = " , ogreHp)
        print("You killed the ogre")
        print("You continue through the forrest")
        room7()

def room5():
     global health, attack, defense, magic
     print(" ") 
     print("You find yourself in a room full of ice")
     print("See 2 Ice Ogres and you start a battle")
     print("*A mysterous voice whispers,'Fire is very effective on Ice beasts.'")
        
     fight1 = input ("What do you do? Chose you wepon. Fire blast. ")

     if fight1.upper()[0] == "F":
         print("You shoot your fire blast and it hits both ogers killing them instently")
         IogerHp = 0
         Ioger2Hp = 0
         print("Ice Oger1 health = " , IogerHp)
         print("Ice Oger2 health = " , Ioger2Hp)
         print("You level up in magic")
         magic = 4
         print("magic = ", magic)
         room6()
         
         
def room6():
    global health, attack, defense, magic, Shrek
    
    print(" ")
    print("You go through a door and find yourself in a forrest.")
    print("After a short walk you come across a cave and decide to enter")
    print("Inside you find the great, green Ogre know only as Shrek")
    print("He roars a might roar,'What are ya doin in me swamp! I will kill you!' ")
    print("You engage in a battle with the might Shrek")

    while health > 0 and Shrek > 0:
        print("Choose your weapon:")
        print("F:Fire Blast")
        print("S:Rusty Sword")
        if health <= 10:
            print("You find a health potion on the floor and drink it")
            health = health + 10
            print("Hp =", health)
        fightboss = input ("What do you do?  ")

        if fightboss.upper()[0] == "F":
            print("You shoot your fire blast and it hits Shrek in the stomach")
            Shrek = Shrek - 10
            print("Shrek Hp = ", Shrek)
            print("Shrek slams his fist down on you")
            health = health - 5
            print("Hp = ", health)

        elif fightboss.upper()[0]=="R":
            print("You swipe your sword and get a hit in Shrek's leg")
            Shrek = Shrek-5
            print("Shrek Hp = ", Shrek)
            print("Shrek stomps on you")
            health = health - 10
            print("Hp = ", health)
        if Shrek <= 0:
            print("You defeated the mighty Shrek and see the chest he was gurding")
            print ("You deside to open it and and find ...  the legendery sword known as the Shreker and the great armor of Shrek.")
            attack = 100
            defence = 100
            print("Attack Damage = ", attack)
            print("Defence level = ", defence)

            print("After a long journey you deside to head home with all you new lit gear and riches.")
            print("                                                                 The End")
            
        
def room7():
    global health, attack, defense, magic, Shrek
    
    print(" ")
    print("After a short walk you come across a a small houseand enter")
    print("Inside you find a crossbow and a bunch of arrows")
    print("You continue on your way")
    attack= 25
    room8()


    
def room8():
    global health, attack, defense, magic, Shrek
    
    print(" ")
    print("After a while you come acroos a cave and deside to enter")
    print("Inside you find the great, green Ogre know only as Shrek")
    print("He roars a might roar,'What are ya doin in me swamp! How dare you steal my axe and onions! I will kill you!' ")
    print("You engage in a battle with the might Shrek")

    while health > 0 and Shrek > 0:
        print("Choose your weapon:")
        print("A:Battle Axe")
        print("C:CrossBow")
        if health <= 10:
            print("You find a health potion on the floor and drink it")
            health = health + 10
            print("Hp =", health)
        fightboss = input ("What do you do?  ")

        if fightboss.upper()[0] == "C":
            print("You shoot your crossbow and it hits Shrek in the stomach")
            Shrek = Shrek - 5
            print("Shrek Hp = ", Shrek)
            print("Shrek slams his fist down on you")
            health = health - 5
            print("Hp = ", health)

        elif fightboss.upper()[0]=="A":
            print("You swipe your battle axe and hit Shrek's leg")
            Shrek = Shrek-10
            print("Shrek Hp = ", Shrek)
            print("Shrek stomps on you")
            health = health - 10
            print("Hp = ", health)
        if Shrek <= 0:
            print("You defeated the mighty Shrek and see the chest he was gurding")
            print ("You deside to open it and and find ...  the legendery sword known as the Shreker and the great armor of Shrek.")
            attack = 100
            defence = 100
            print("Attack Damage = ", attack)
            print("Defence level = ", defence)

            print("After a long journey you deside to head home with all you new lit gear and riches.")
            print("                                                                 The End")    
    
    
        

  


    
   
                   
    
        
              
            
            
            
        
    
    #... make a game








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    startingroom()
    
    
    
    
