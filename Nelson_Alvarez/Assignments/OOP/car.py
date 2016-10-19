class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.speed = speed 
        self.fuel = fuel
        self.mileage = mileage
        self.price = price
        if price > 10000:
           self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print 'Price: $', self.price
        print 'Speed: ', self.speed 
        print 'Fuel: ', self.fuel
        print 'Mileage: ', self.mileage 
        print 'Tax: ', self.tax
        
Ford = Car(2000, 35, 'Full', 15)
Chevy = Car(2000, 5, 'Not Full', 105)
Nissan = Car(2000, 15, 'Kind of Full', 95)
Toyota = Car(2000, 25, 'Full', 25)
Fiat = Car(2000, 45, 'Empty', 25)
Lambo = Car(20000000, 35, 'Empty', 15)