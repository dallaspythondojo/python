from animal import Animal
class Dog(Animal):
    def __init__(self, name=None):
        super(Dog, self).__init__()
        self.health = 150
        self.name = name
    def pet(self):
        self.health += 5
        print "That's the spot, human"
dog = Dog('Fred')
dog.walk().walk().walk().run().run().pet()
dog.displayHealth()
