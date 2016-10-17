from humane import Human
class Wizard(Human):
  def heal(self):
	self.health += 10
class Ninja(Human):
  def steal(self):
	self.stealth += 5
class Samurai(Human):
  def sacrifice(self):
	self.health -= 5
# create new instance of Wizard, Ninja, and Samurai
harry = Wizard()
rain = Ninja()
tom = Samurai()
# all instances still have human properties because its
# class inherits from the Human class
print harry.health
print rain.health
print tom.health
# yet they are subclasses which mean they can extend the current functionality of Human class
# instances of the Wizard class can perform the heal method
harry.heal()
print harry.health
# instances of the Ninja class can perform the steal method
rain.steal()
print rain.stealth
# instances of the Samurai class can perform the sacrifice method
tom.sacrifice()
print tom.health
print tom.stealth
print tom.attack()