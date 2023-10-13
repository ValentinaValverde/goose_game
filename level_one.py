from characters import Goose, Pigeon
goose = Goose("goose", 100, 50)
pigeon = Pigeon("pigeon", 50, 20)


print(" ")
print("Welcome to HONK!")
print("you are a goose.")
print("you cause chaos.")
print("are you the superior bird?")
print("let's find out!")
print("type 'HONK' to begin.")

start = input("> ")


def begin_game():
    print("you are a goose")
    print("you see a pigeon.")
    print("what will you do?")


if start == "HONK" or start == "honk":
    begin_game()
else:
    print("invalid input. game over, sorry!")



while pigeon.alive() and goose.alive():
    print("1. attack pigeon")
    print("2. scare pigeon")
    print("3. fly away")

    choose_one = input("> ")

    if choose_one == "1" or choose_one == "attack" or choose_one == "attack pigeon":
        print("you've chosen the path of violence")
        goose.attack(pigeon)

    elif choose_one == "2" or choose_one == "scare" or choose_one == "scare pigeon":
        print("you've chosen to be spooky")
        goose.honk(pigeon)

    elif choose_one == "3" or choose_one == "fly away":
        print("you're a coward.")

    else:
        print("invalid input. game over, sorry!")
