class Animal(object):
	def __init__(self, name, health=100):
		self.name = name
		self.health = health 

	def walk(self, m=1):
		
		self.health -= 1 * m
		return self
	
	def run(self, m=1):
		self.health -= 5 * m
		return self

	def displayHealth(self):
		print 'Name:', self.name
		print 'Health:', self.health 
		return self 

animal = Animal('Animal')
animal.walk(3).run(2).displayHealth()


class Dog(Animal):
	def __init__(self,name):
		print 'My Pet Dog'
		super(Dog, self).__init__(name)
		self.health = 150
	
	def pet(self):
		self.health += 5 
		return self

dog = Dog('Pooch')
dog.walk(3).run(2).pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print 'Pet Dragon'
        super(Dragon, self).displayHealth()

dragon = Dragon('Firefly')
dragon.fly().displayHealth()