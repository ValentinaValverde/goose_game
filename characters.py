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
    
    def attack(self, opponent):
        print("%s has attacked %s!" % (self.name, opponent.name))
        opponent.health -= self.power
        print("%s now has %s health!" % (opponent.name, opponent.health))
        print(" ")


class Goose(Bird):
    def honk(self, opponent):
        print("you've deeply frightened %s!" % opponent.name)
        print("%s has flown away!" % opponent.name)


class Pigeon(Bird):
    def come_back(self):
        print("oh no! %s has come back with a friend!" % self.name)


    
