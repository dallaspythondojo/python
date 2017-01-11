class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if self.price > 10000:
            self.tax = 0.15
    def display_all(self):
        print 'Price: {}'.format(self.price)
        print 'Speed: '+self.speed
        print 'Fuel: {}'.format(self.fuel)
        print 'Mileage: {}'.format(self.mileage)
        print 'Tax: {}'.format(self.tax)

car1 = car(2000, '35mph', 'Full', '15mpg')
car2 = car(2000, '5mph', 'Not Full', '105mpg')
car3 = car(20000, '90mph', 'Full', '30mpg')
car4 = car(10000, '80mph', 'Not Full', '45mpg')
car5 = car(5000, '50mpg', 'Not Full', '60mpg')
car6 = car(1000, '60mpg', 'Empty', '30mpg')

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
