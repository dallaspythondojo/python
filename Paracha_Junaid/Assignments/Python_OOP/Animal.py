class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def displayHealth(self):
		print self.name
		print self.health
		return self
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self

# ani1 = Animal('cat')
# ani1.displayHealth()
# ani1.walk()
# ani1.displayHealth()
# ani1.run()
# ani1.displayHealth()


# animal = Animal('Animal')
# animal.walk().walk().walk().run().run().displayHealth()

# Create an instance of the animal called 'animal' and 
# have this animal walk three times, run twice, and have it display its health.
