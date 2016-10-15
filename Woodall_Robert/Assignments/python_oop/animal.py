class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	
	def walk(self):
		print('walking...(-1)')
		self.health -= 1
		
		return self
	
	def run(self):
		print('running...(-5)')
		self.health -= 5
		
		return self
	
	def display_health(self):
		print(('{}\'s health: {}').format(self.name, self.health))
		
		return self

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
		
	def pet(self):
		print('petting...(+5)')
		self.health += 5
		
		return self
	
class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
		
	def fly(self):
		print('flying...(-10)')
		self.health -= 10
		
		return self
	
	def display_health(self):
		print('This is THE dragon!')
		super(Dragon, self).display_health()
		
		return self
	
animal = Animal('Animal')
animal.display_health().walk().walk().walk().run().run().display_health()

print
peanut = Dog('Peanut')
peanut.display_health().walk().walk().walk().run().run().pet().display_health()

print
bruce = Dragon('Bruce Lee')
bruce.display_health().walk().walk().walk().run().run().fly().fly().display_health()
