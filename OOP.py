
class Game:
    variable1 = 'Hello'
    variable2 = 'World'


# Parent Class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def Information(self):
        msg = "\nName: {},\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# Child Class Instance
class Human(Organism):
    name = 'Trevor'
    species = 'Homosapian'
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

# Another child class instance
class Dog(Organism):
    name = "Spot"
    species = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferotiously on its target!"
        return msg
# Another Child Class Instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two dseperate organisms!"
        return msg










if __name__ == "__main__":
    #OOP Part1
    x = Game()
    print("{} {}".format(x.variable1,x.variable2))
    #OOP Part2
    human = Human()
    print(human.Information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.Information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.Information())
    print(bacteria.replication())
