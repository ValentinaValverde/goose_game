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
    print("1. attack pigeon")
    print("2. scare pigeon")
    print("3. fly away")
    choose_one = input("> ")

    if choose_one == "1" or choose_one == "attack" or choose_one == "attack pigeon":
        print("you've chosen the path of violence")

    elif choose_one == "2" or choose_one == "scare" or choose_one == "scare pigeon":
        print("you've chosen to be spooky")

    elif choose_one == "3" or choose_one == "fly away":
        print("you're a coward.")

    else:
        print("invalid input. game over, sorry!")



if start == "HONK" or start == "honk":
    begin_game()
else:
    print("invalid input. game over, sorry!")



