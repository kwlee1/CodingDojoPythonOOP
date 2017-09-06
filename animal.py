class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1 
        return self 

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.health
        return self 

animal1 = Animal("Nox",100)
animal1.displayHealth()
animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.displayHealth() 

class Dog(Animal):
    def __init__(self,name,health):
        super(Dog,self).__init__(name,health)
        self.health = 150     
    def pet(self):
        self.health += 5

animal2 = Dog("Winston",100)
animal2.displayHealth()
animal2.walk()
animal2.walk()
animal2.walk()
animal2.run()
animal2.run()
animal2.pet()
animal2.displayHealth()

class Dragon(Animal):
    def __init__(self,name,health):
        super(Dragon,self).__init__(name,health)
        self.health = 170
    
    def fly(self):
        self.health -= 10
    
    def seeHealth(self):
        super(Dragon,self).displayHealth()
        print "I am a Dragon"

animal3 = Dragon("Shenron",100)
animal3.seeHealth()
animal3.fly()
animal3.seeHealth()

animal2.fly()
# Result is: AttributeError: 'Dog' object has no attribute 'fly'