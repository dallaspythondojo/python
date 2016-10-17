from animal import Animal
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__()
        self.health = 170
        self.name = name
    def displayHealth(self):
        print 'this is a dragon'
        super(Dragon, self).displayHealth()
    def fly(self):
        self.health -= 10
        print "You have such large wings.."
        return self
dragon = Dragon('Joey Anne')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
