class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		print "{} is walking...".format(self.name)
		self.health -= 1
		return self

	def run(self):
		print "{} is running...".format(self.name)
		self.health -=5
		return self

	def displayHealth(self):
		print "{} has a {} health.".format(self.name, self.health)
		return self

class Dog(Animal):
	def __init__(self, name):		
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		print "You have just petted {}".format(self.name)
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self,name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		print "{} is now flying".format(self.name)
		self.health -= 10
		return self

	def displayHealth(self):
		print "This is a dragon!"
		super(Dragon, self).displayHealth()
		return self


animal1 = Animal('Ke$ha')
animal1.walk().walk().walk().run().run().displayHealth()

dog1 = Dog("doggo")
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Trogdor")
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
