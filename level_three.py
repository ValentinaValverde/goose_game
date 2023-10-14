from characters import Goose, Duck
goose = Goose("goose", 150, 50)
duck = Duck("duck", 100, 50)



def goose_vs_duck():
    print(" ")
    print(" (o<     !    <o)")
    print("<_)            (_>")
    print(" ")


def dead_goose():
    print(" ")  
    print(" (x<")
    print("<_)")
    print(" ")


while duck.alive() and goose.alive():
    print(" ")
    print("1. attack duck")
    print("2. scare duck")
    print("3. fly away")

    choice = input("> ")


    if choice == "1" or choice == "attack" or choice == "attack duck":
        print("you've chosen the path of violence")
        goose.attack(duck)
        print(" ")

        if duck.alive():
            duck.attack(goose)
            print(" ")


    elif choice == "2" or choice == "scare" or choice == "scare duck":
        print("you've chosen to be spooky")
        print("duck seems to be unafraid.")
        print(" ")

        duck.attack(goose)
        print(" ")


    elif choice == "3" or choice == "fly away":
        print(" ")
        print("coward.")
        print(" ")
        break

    else:
        print("invalid input. game over, sorry!")
        break
