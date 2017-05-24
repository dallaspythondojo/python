class Car(object):
	def __init__(self, price, speed, fuel, mileage, tax=0.12):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax
	def display_all(self):
		print'Price = ', self.price
		print'Speed = ', self.speed
		print'Fuel = ', self.fuel
		print'Mileage = ', self.mileage
		print'tax = ', self.tax

a=Car(2000,35,'full',15)
a.display_all()

b=Car(2000,5,'not_full',105)
b.display_all()

c=Car(2000,15,'kind_of_full',95)
c.display_all()

d=Car(2000,25,'full',25)
d.display_all()

f=Car(2000,45,'empty',25)
f.display_all()

g=Car(20000000,35,'empty',15, 0.15)
g.display_all()