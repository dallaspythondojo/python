class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayhealth(self):   #display on screen the name of the animal and the health
		print self.name + " " + str(self.health)

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health =150

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		 
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayhealth(self):
		print 'this is a dragon'
		super(Dragon,self).displayhealth()
		return self



animal = Animal("dog")
animal.displayhealth()
animal.walk().walk().walk().run().run().displayhealth()

dog = Dog("pulgoso")
dog.walk().walk().walk().run().run().pet().displayhealth()

my_dragon= Dragon("snoopy")
my_dragon.fly().fly().fly().run().run().fly().fly().displayhealth()




