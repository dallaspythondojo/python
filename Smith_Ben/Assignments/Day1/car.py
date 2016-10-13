class Car(object):
  def __init__(self, price, speed, fuel, mileage=200):
    print "Production Line"
    self.price = price
    self.speed = str(speed)
    self.fuel = str(fuel)
    self.mileage = str(mileage)
    self.tax = '12'
    if self.price > 10000:
      self.tax = '15'
      self.price = str(price)

  def display_all(self):
    print 'Price', self.price
    print 'Speed', self.speed +'mph'
    print 'Fuel', self.fuel 
    print 'Mileage', self.mileage + 'mpg'
    print 'Tax', self.tax + '%'


Ben=Car(20000, 200, 'half')
Ben.display_all()


Ford = Car(40000, 150, 'Half', 30)
Ford.display_all()

GMC = Car(5000, 80, 'Full', 27)
GMC.display_all()

Subaru = Car(90000, 70, 'Quarter', 45)
Subaru.display_all()

Dodge = Car(8000, 70, 'Full', 12)
Dodge.display_all()

Ram = Car(12000, 120, 'Full', 44)
Ram.display_all()

Ferarri = Car(300000, 250, 'Full', 12)
Ferarri.display_all()
