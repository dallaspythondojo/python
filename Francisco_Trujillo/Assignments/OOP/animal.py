class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name
        
    def walk(self):
        self.health-=1
        return self
    
    def run(self):
        self.health-=5
        return self
    
    def displayHealth (self):
        print("The animal's name is " + self.name + " and has a health of " + str(self.health) + " points")

        return self
    
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
        
    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
        
    def fly(self):
        self.health-=10
        return self
    
    def displayHealth(self):
        print('This is a Dragon')
        super(Dragon,self).displayHealth()
    
print('Animal')
animal = Animal('animal')
animal.walk().walk().walk().run().run().displayHealth()
print

print('Dog')
careto = Dog("Careto")
careto.walk().walk().walk().run().run().pet().displayHealth()
print

print("Dragon")
saphira = Dragon("Saphira")
saphira.walk().walk().walk().run().run().fly().displayHealth()



