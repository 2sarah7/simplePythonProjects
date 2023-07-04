
import time
import random
inventory = ["Hands"]

def youDied():
        print("You died. ")
        quit()

def sptContd():
        print("There is an army of aliens attacking the city! People are trying to fight them but the aliens are overpowering them.")
        if "sword" in inventory:
                askk = input("Do you want to use your sword? ")
                if "yes" in askk.lower():
                        print("You fought very bravely and with the help of the other people, you were able to defeat the aliens!")
                        time.sleep(1)
                        print("With your help, the world was saved!")
                else:
                        print("The aliens killed you. ")
                        youDied()
        else:
                        print("The aliens killed you. ")
                        youDied()

def storyPtTwo():
        print("As you were running, you see and abandoned bag.")
        kdkdkdk = input("Do you want to pick it up? ")
        if kdkdkdk.lower() in ["yes", "take bag", "pick up bag", "bag"]:
                print("In the bag there is a sword!")
                time.sleep(1)
                inventory.append("sword")
                print("The sword was added to your inventory.")
        else:
                print("You continue without observing the bag. ")
        time.sleep(1)
        asin = input("You see an alien ship suddenly come our of the sky! It looks like they're about to attack the city! Do you want to go over there and see what is going on? ")
        if asin.lower() in ["yes", "go to city", "see", "see what is going on", "city"]:
                print("You run over to where the spaceship is landing.")
                sptContd()
        else:
                print("You didn't go to see what was going on and you let the aliens destroy everything. ")
                youDied()

def storyPtOne():
        time.sleep(1)
        health = 100
        monsterHealth = 100
        print("Suddenly you see a big dog-like monster. ")
        print("The only weapon you have is your hands.")
        time.sleep(1)
        health = health - random.randint(1,10)
        print("The monster attacked you! Your health is now", str(health)+ ".")
        time.sleep(1)
        monsterHealth = 50
        print("You attacked the monster! His health is now ", str(monsterHealth)+ ".")
        time.sleep(1)
        print("You expertly dodge the next attack and are able to kill the monster. ")
        print("Once you kill him, you run away as fast as you can from the area.")
        storyPtTwo()
        
def desk():
        print("You go up to the strange person at the desk and ask what this building is. ")
        time.sleep(2)
        print("They say to look behind you. That is kinda suspicious... ")
        storyPtOne()

def elevator():
        jkl = input("What floor do you want to go to?")
        print("Going to floor", jkl+ "...")
        time.sleep(5)
        print("The elevator door opens")
        storyPtOne()

def car():
        print("You get into the taxi car. The driver drives off without asking where you want to go. ")
        time.sleep(5)
        print("The driver drops you off at a forest and speeds away. ")
        storyPtOne()

def building():
        print("It is a large skyscraper. Inside, you see an elevator and a desk with a receptionist (who kinda looks like an alien). ")
        def q2():
                tttt = input("What do you want to do? ")
                if tttt.lower() in ["elevator", "go to elevator", "i want to go to the elevator"]:
                        elevator() 
                elif tttt.lower() in ["desk", "go to desk", "go to the desk", "receptionist", "alien"]:
                        desk()
                elif tttt.lower() in ["door", "back", "behind", "go back", "go behind", "go to the door", "go back to the door"]:
                        print("The door is locked. You can't leave. ")
                else:
                        print("Sorry, I don't understand that. Try again. ")
                        q2()
        q2()


def intro():
        name = input("What is your name? ")
        print("Hello,", name+ ", welcome to the future! ")
        time.sleep(1)
        print("Here are some helpful commands that you can use in the game: \n go to <place> \n take <object> \n chose <object>")
        time.sleep(4)
        print("Let's begin... ")
        time.sleep(1)
        print("You are in a future United States. It is the year 5035. It is a lot different than what you may think. Society is a mess. Other planets are planning to invade earth. It is your job to help save earth. ")
        time.sleep(5)
        def q1():
                asdf = input("In front of you is a large building \n and to your right there is a car. \n Do you want to go in the car or the building? ")

                if asdf.lower() in ["go to car", "car", "vehicle", "right"]:
                       car()
                elif asdf.lower() in ["go to building", "building", "front", "forward", "door", "building door"]:
                       building()
                else:
                        print("Sorry, I can't understand that. Please try again. ")
                        time.sleep(2)
                        q1()
        q1()


intro()