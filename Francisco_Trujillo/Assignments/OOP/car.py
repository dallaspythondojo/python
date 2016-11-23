class Car(obeject):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if self.price > 10000:
            self.tax = 0.15
        else: self.tax = 0.12
        
        
    
    def display_all(self):
        print "Price: " +str(self.price)
        print "Spped: "+str(self.speed)
        print "Fuel: "+str(self.fuel)
        print "Milage: "+str(self.milage)
        print "Tax: "+str(self.tax)
        return self
        
car1 = Car(2000, "35mph", "Full", "15mpg")
car1.display_all()

car2 = Car(2000, "5mph", "Not Full", "105mpg")
car1.display_all()

car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
car3.display_all()

car4 = Car(2000, "25mph", "Full", "25mpg")
car4.display_all()

car5 = Car(2000, "45mph", "Empty", "25mpg")
car5.display_all()

car6 = Car(20000000, "35mph", "Empty", "15mpg")
car6.display_all()