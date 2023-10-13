class Bird:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            print("%s has %d health and %d power." % (self.name, self.health, self.power))
        else:
            print("you've been died!")
        return self.health


class Goose(Bird):
    def attack(self, opponent):
        print("you have attacked %s!" % opponent.name)
        opponent.health -= self.power

    def honk(self, opponent):
        print("you've deeply frightened %s!" % opponent.name)


goose = Goose("goose", 100, 50)
