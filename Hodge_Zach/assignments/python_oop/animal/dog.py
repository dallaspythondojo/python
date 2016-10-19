from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog = Dog("Rex")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon!"
        print "Name: " + self.name
        print "Health: " + str(self.health)

dragon = Dragon("Tanis")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
