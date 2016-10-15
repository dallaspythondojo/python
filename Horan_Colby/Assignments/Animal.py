class Animal(object):
	def __init__(self, name):
		self.health = 100
		self.name = name

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print "Animal: " + self.name
		print "Health: " + str(self.health)
		return self

class Dog(Animal):
	def __init__(self):
		self.health = 150
		self.name = 'Dog'

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self):
		self.health = 170
		self.name = 'Dragon'

	def fly(self):
		self.health -=  10
		return self

	def displayHealth(self):
		print "This is a dragon!"
		print "Animal: " + self.name
		print "Health: " + str(self.health)
		return self

animal = Animal('Animal')
animal.walk().walk().walk().run().run().displayHealth()


dog = Dog()
dog.walk().walk().walk().run().run().pet().displayHealth()


dragon = Dragon()
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
