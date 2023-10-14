from characters import Goose, Pigeon

goose = Goose("goose", 100, 50)
pigeon = Pigeon("pigeon", 50, 20)


print(" ")
print("Welcome to HONK!")
print("you are a goose.")
print("you cause chaos.")
print(" ")
print("are you the superior bird?")
print("let's find out!")
print(" ")
print("type 'HONK' to begin.")

start = input("> ")


def begin_game():
    print(" ")
    print("you are a goose.")
    print("you see a pigeon.")
    print("what will you do?")
    print(" ")



if start == "HONK" or start == "honk":
    begin_game()
else:
    print("do you know how to spell???")



pigeon_array = [pigeon]

# if pigeon.alive() and goose.alive():
while len(pigeon_array) > 0 and goose.alive():
    print(" ")
    print("1. attack pigeon")
    print("2. scare pigeon")
    print("3. fly away")

    choose_one = input("> ")


    if choose_one == "1" or choose_one == "attack" or choose_one == "attack pigeon":
        print("you've chosen the path of violence")
        goose.attack(pigeon_array[0])

        #deleting a pigeon from the array each time goose attacks
        del(pigeon_array[0])
        print(pigeon_array)


    elif choose_one == "2" or choose_one == "scare" or choose_one == "scare pigeon":
        print("you've chosen to be spooky")
        goose.honk(pigeon)
        print(" ")

        print("oh no! pigeon has returned with a friend!")
        pigeon_array.append(pigeon)
        print(" ")

        pigeon.attack(goose)


    elif choose_one == "3" or choose_one == "fly away":
        print(" ")
        print("you're a coward.")
        print(" ")
        break

    else:
        print("invalid input. game over, sorry!")
        break
