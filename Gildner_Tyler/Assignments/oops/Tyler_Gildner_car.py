class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        print 'nice car bro'
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if self.price > 10000:
            self.tax = 0.15
    def display(self):
        print 'price',self.price
        print 'speed',self.speed
        print 'fuel',self.fuel
        print 'mileage',self.mileage
        print 'tax',self.tax

honda = Car(4000, 55, 'low', 20)

honda.display()

ford = Car(11000, 30, 'full', 13)

ford.display()

saturn = Car(9000, 40, 'half', 24)

saturn.display()

acura = Car(17000, 70, 'three quarters', 21)

acura.display()

toyota = Car(3000, 25, 'low', 19)

toyota.display()

bmw = Car(28000, 90, 'full', 23)

bmw.display()
