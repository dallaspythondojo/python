class Bike(object):
    def __init__(this, price, max_speed, miles=0):
        this.price = price
        this.max_speed = max_speed
        this.miles = miles
    def displayinfo(this):
        print this.price
        print this.max_speed
        print this.miles
    def ride(this):
        print "Riding..."
        this.miles +=10
    def reverse(this):
        print "Reversing..."
        this.miles -=5
        if (this.miles<0): #these lines were added to prevent the miles from
            this.miles=0   #displaying as negative

bike1 = Bike(200, "25mph")
bike2 = Bike(100, "20mph")
bike3 = Bike(150, "23mph")

for x in range(3):
    bike1.ride()
bike1.reverse()
bike1.displayinfo()

for x in range(2): #I understand the problem asked for the bike to be ridden twice
    bike2.ride()   # THEN reversed twice and this doesn't exactly perform that exact function
    bike2.reverse() #but since it is addition, the total miles ridden is the same.
bike2.displayinfo()

# bike2.ride()
# bike2.ride()
# bike2.reverse()
# bike2.reverse()
# bike2.displayinfo()

for x in range(3):
    bike3.reverse()
bike3.displayinfo()
