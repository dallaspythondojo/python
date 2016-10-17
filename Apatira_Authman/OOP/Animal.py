class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = str(name)

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.name
        print 'Health :' + str(self.health)
        return self



class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

    def displayHealth(self):
        print str(self.name)

animal = Animal('Troy')

animal.walk().walk().walk().run().run().displayHealth()

mj = Dog('Swaggy')

mj.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon,self).displayHealth()
        print 'This is a dragon!'
        return self


slayer = Dragon('Puff')
slayer.walk().walk().walk().run().run().fly().fly().displayHealth()
