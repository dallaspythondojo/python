class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self, x=1):
		self.health -= 1 * x
		return self

	def run(self, r=1):
		self.health -= 5 * r
		return self

	def displayHealth(self):
		print self.name
		print self.health
		return self



animal = Animal('Brutus')
animal.walk(3).run(2).displayHealth()

class Dog(Animal):
	def __init__(self, name='Tom'):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

animal2 = Dog('Harvey')
animal2.walk(3).run(2).pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name="Scaley"):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self, f=1):
		self.health -= 10 * f
		return self

	def displayHealth(self):
		print 'This is a Dragon'
		super(Dragon, self).displayHealth()
		return self

animal3 = Dragon('Moose')
animal3.walk(3).run(2).fly(2).displayHealth()






