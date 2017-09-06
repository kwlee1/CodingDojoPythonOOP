class MathDojo(object):
    def __init__(self):
        self.sum = 0 
    def add(self,*args):
        self.tuple = args
        for num in self.tuple:
            if type(num) is int or type(num) is float:
                self.sum += num
            if type(num) is list: 
                for x in num: 
                    self.sum += x 
            if type(num) is tuple:
                for el in num:
                    if type(el) is int or type(el) is float: 
                        self.sum += el 
                    if type(el) is list: 
                        for x in el: 
                            self.sum += x 
        return self 
    def subtract(self,*args):
        self.tuple = args  
        for num in self.tuple: 
            if type(num) is int or type(num) is float: 
                self.sum -= num 
            if type(num) is list: 
                for x in num: 
                    self.sum -= x 
            if type(num) is tuple: 
                for el in num: 
                    if type(num) is int or type(num) is float: 
                        self.sum -= el 
                    if type(num) is list:
                        for x in el: 
                            self.sum -= x 
        return self 
    def result(self):
        print self.sum 

md = MathDojo() 
# md.add(2).add(2,5).subtract(3,2).result()
md.add([1],2.5, 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2,2.5, [2,3], [1.1,2.3]).result()
