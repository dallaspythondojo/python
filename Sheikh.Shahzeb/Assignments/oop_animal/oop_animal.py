class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name,health=100):
		super(Animal, self).__init__()
		self.name = name
		self.health= health
	def walk(self):
		self.health -=1
		return self
	def run(self):
		self.health -=5
		return self
	def display_health(self):
		print(self,'health - ',self.health )
		return self

animal = Animal('cheetah')
animal.walk().walk().walk().run().run().display_health()

class Dog(Animal):
	"""docstring for cheetah"""
	def __init__(self,name,health= 150):
		super(Dog, self).__init__(name)
	def pet(self):
		self.health+=5
		return self

leo = Dog('Leo')
leo.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self,name, health= 170):
		super(Dragon, self).__init__(name)
		self.health= health
	def fly(self):
		self.health-=10
		return self
dragon = Dragon('Roy')
dragon.walk().walk().walk().run().run().fly().fly().display_health()

		

		

			
		