#to upgrade this game, have it so that the goose can have a battle with
#the rooster after the chicken dies.
#rn it's set up so that the rooster instantly kills the goose.

from characters import Goose, Chicken, Rooster

goose = Goose("goose", 100, 50)
chicken = Chicken("chicken", 50, 25)
rooster = Rooster("rooster", 100, 100)


def goose_vs_chicken():
    print(" ")
    print(" (o<    !     <o)")
    print("<_)            (v)")
    print(" ")


def goose_vs_rooster():
    print("              ,")  
    print(" (o<    !    <o)")
    print("<_)           (v)")
    print(" ")


def dead_goose():
    print(" ")  
    print(" (x<")
    print("<_)")
    print(" ")


print(" ")
print("you are a goose.")
print("you see a chicken.")
goose_vs_chicken()
print("what will you do?")
print(" ")

#idea: at the beginning of the game, have the goose img and the opponent img stare at each other!

while chicken.alive() and goose.alive():
    print(" ")
    print("1. attack chicken")
    print("2. scare chicken")
    print("3. fly away")


    choice = input("> ")


    if choice == "1" or choice == "attack" or choice == "attack chicken":
        print("you've chosen the path of violence")
        goose.attack(chicken)
        print(" ")

        print("a rooster appears")
        goose_vs_rooster()        
        rooster.attack(goose)

        dead_goose()
        print("you've died.")
        print("you are not the superior bird.")


    elif choice == "2" or choice == "scare" or choice == "scare chicken":
        print("you've chosen to be spooky")
        chicken.lay_egg()
        print(" ")



    elif choice == "3" or choice == "fly away":
        print(" ")
        print("coward.")
        print(" ")
        break

    else:
        print("invalid input. game over, sorry!")
        break