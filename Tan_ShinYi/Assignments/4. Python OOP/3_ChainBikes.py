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
        return this
    def reverse(this):
        print "Reversing..."
        this.miles -=5
        if (this.miles<0): #these lines were added to prevent the miles from
            this.miles=0   #displaying as negative
        return this

bike1 = Bike(200, "25mph")
bike2 = Bike(100, "20mph")
bike3 = Bike(150, "23mph")

bike1.ride().ride().ride().reverse().displayinfo()

bike2.ride().ride().reverse().reverse().displayinfo()

bike3.reverse().reverse().reverse().displayinfo()
