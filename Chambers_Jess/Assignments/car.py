
class car(object):
    def __init__(self, price, speed, fuel, mileage):
        print 'New Car'
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax: ", self.tax
        return self

car1 = car(12000, 120, 'Full', '15mpg')
car1.display_all()

car2 = car(12000, 120, 'Full', '15mpg')
car2.display_all()

car3 = car(15000, 150, 'Empty', '25mpg')
car3.display_all

car4 = car(7000, 100, 'Half Full', '15mpg')
car4.display_all()

car5 = car(4000, 40, 'Full', '20mpg')
car5.display_all()

car6 = car(2000, 112, 'Full', '15mpg')
car6.display_all()
