class Car(object):
    def __init__(this, price, speed, fuel, mileage):
        this.price = price
        this.speed = speed
        this.fuel= fuel
        this.mileage= mileage
        if price>10000:
            this.tax= 0.15
        else:
            this.tax= 0.12
        this.display_all()
    def display_all(this):
        print "Price: " + str(this.price)
        print "Speed: " + str(this.speed) +"mph"
        print "Fuel: " + this.fuel
        print "Mileage: " + str(this.mileage) +"mpg"
        print "Tax: " + str(this.tax)

car1 = Car(2000, 35, "Full", 15)
car2 = Car(2000, 5, "Not Full", 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(20000000, 35, "Empty", 15)
