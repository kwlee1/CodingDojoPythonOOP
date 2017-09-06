class Bike(object):
    def __init__(self, price, max):
        self.price = price
        self.max = max
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max
        print self.miles 
    def ride(self): 
        print "Riding"
        self.miles += 10 
    def reverse(self):
        print "Reversing"
        # added if statement to prevent miles from going negative
        if self.miles >= 5: 
            self.miles -= 5 

bike1 = Bike(500,20)
bike2 = Bike(300,10)
bike3 = Bike(100,10)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.displayInfo()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()