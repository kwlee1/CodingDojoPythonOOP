class Product(object):
    def __init__(self,price,name,weight,brand,cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost 
        self.status = "for sale"
        

    def sold(self):
        self.status = "sold"
        return self 

    def addTax(self,tax):
        self.price = self.price * (1 + tax)
        return self 

    def refund(self,reason):
        self.reason = reason 
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        if self.reason == "in the box":
            self.status = "for sale"
        if self.reason == "box opened":
            self.price = self.price * 0.8 
            self.status = "used"
        return self 

    def displayInfo(self):
        print self.price
        print self.name
        print self.weight
        print self.brand 
        print self.cost 
        print self.status 
        

item1 = Product(100,"box",15,"Rubik",20)
item1.sold()
item1.addTax(.09)
item1.refund ("in the box")
item1.displayInfo()
item1.sold()
item1.refund("box opened")
item1.displayInfo()
item1.sold
item1.refund("defective")
item1.displayInfo()