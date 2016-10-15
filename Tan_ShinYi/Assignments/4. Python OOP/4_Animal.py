class Animal(object):
    def __init__ (this, name):
        this.name = name
        this.health = 100
    def walk(this):
        this.health -=1
        return this
    def run(this):
        this.health -=5
        return this
    def displayHealth(this):
        print this.name
        print "Health: " + str(this.health)

animal=Animal("Spotty")

animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(this, name): #note to self: remember this syntax and what you have to pass in
        super(Dog, this).__init__(name) #even here, make sure you're passing in the variables you'll need
        this.health=150
    def pet(this):
        this.health +=5
        return this

dog=Dog("Leon")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(this, name):
        super(Dragon, this).__init__(name)
        this.health=170
    def fly(this):
        this.health -=10
        return this
    def displayHealth(this):
        print "This is a dragon!"
        super(Dragon, this).displayHealth()

dragon=Dragon("Drogon")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

# animal.pet() # test cases to make sure that animal does not have these methods
# animal.fly() # which it doesn't because when these lines are run, an error message is returned
# animal.displayHealth()
