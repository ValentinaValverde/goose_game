class Bird:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            print("%s has %d health and %d power." % (self.name, self.health, self.power))
        else:
            print("%s has been died!" % self.name)
        return self.health


class Goose(Bird):
    def attack(self, opponent):
        print("you have attacked %s!" % opponent.name)
        opponent.health -= self.power
        print(opponent.health)

    def honk(self, opponent):
        print("you've deeply frightened %s!" % opponent.name)
        print("%s has flown away!" % opponent.name)


class Pigeon(Bird):
    def something(self):
        print("something")
    
    