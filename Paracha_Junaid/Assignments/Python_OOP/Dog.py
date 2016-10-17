# Now, create another class called Dog that inherits everything that the Animal does 
# and has, but 1) have the default health be 150 and 
# 2) add a new method called pet, 
# which when invoked, increase the health by 5. 
# Have the Dog walk() three times, run() twice, pet() once, 
# and have it displayHealth().

from Animal import Animal
class Dog(Animal):
	"""docstring for Dog"""
	def heal(self):
		# super(Dog, self).__init__()
		self.health = 150
		return self
	def pet(self):
		self.health +=5
		return self
Dog1 = Dog('Dog1')
print Dog1.heal().walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def heal(self):
		self.health = 170
		return self
	def fly(self):
		print "This is a Dragon"
		self.health -= 10
		return self
Dragon = Dragon('Dragon')
print Dragon.heal().walk().walk().walk().run().run().fly().fly().displayHealth()
