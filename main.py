weapon = False # = 0 Boolean Value

def goblinSlayer():
    actions = ["fight", "flee"]
    global weapon
    print("You find yourself in the depths of a dark and ominous dungeon. The stench of goblins fills the air.")
    print("A horde of goblins approaches. You can either fight them or flee. What would you like to do?")
    userInput = ""
    while userInput not in actions:
        print("Options: flee/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                print("With your trusty sword, you defeat the goblins and continue your quest. Well done, Goblin Slayer!")
                quit()
            else:
                print("You try to fight the goblins barehanded, but they overpower you. You have been defeated.")
                quit()
        elif userInput == "flee":
            showGoblinNest()
        else:
            print("Please enter a valid option.")

def showGoblinNest():
    directions = ["backward", "forward"]
    global weapon
    print("You cautiously make your way deeper into the dungeon and come across the goblin nest.")
    print("Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: backward/forward")
        userInput = input()
        if userInput == "backward":
            goblinSlayer()
        elif userInput == "forward":
            goblinCave()
        else:
            print("Please enter a valid option.")

def goblinCave():
    directions = ["right", "left", "backward"]
    print("You enter a dark cave filled with goblins. You must be careful to survive.")
    print("Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("You venture deeper into the cave, but the goblin's ambush you. You have been defeated.")
            quit()
        elif userInput == "left":
            print("You find a hidden stash of weapons! You now have a sword.")
            weapon = True
        elif userInput == "backward":
            showGoblinNest()
        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    while True:
        print("""
_____         _      _  _          _____  _                               
|  __ \       | |    | |(_)        /  ___|| |                              
| |  \/  ___  | |__  | | _  _ __   \ `--. | |      __ _  _   _   ___  _ __ 
| | __  / _ \ | '_ \ | || || '_ \   `--. \| |     / _` || | | | / _ \| '__|
| |_\ \| (_) || |_) || || || | | | /\__/ /| |____| (_| || |_| ||  __/| |   
\____/ \___/ |_.__/ |_||_||_| |_| \____/ \_____/ \__,_| \__, | \___||_|   
                                                        __/ |            
                                                        |___/             
              """)
        print("Welcome to the Goblin Slayer Adventure Game!")
        print("You are Goblin Slayer, a fearless warrior on a mission to exterminate goblins.")
        print("You find yourself in a dangerous dungeon filled with goblins.")
        print("Let's start your journey. What is your name, Goblin Slayer?")
        name = input()
        print("Good luck, " + name + ".")
        goblinSlayer()
