class Animal(object):
    def __init__(self, name=None):
        print 'very cool animal dude.'
        self.health = 100
        self.name = name
    def walk(self):
        self.health -= 1
        print "You walked 500 miles..."
        return self
    def run(self):
        self.health -= 5
        print "You are running, for some reason"
        return self
    def displayHealth(self):
        print 'name:',self.name
        print 'health:',self.health,
        return self
animal = Animal('bob')
animal.displayHealth()
