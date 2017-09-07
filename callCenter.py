class Call(object):
    def __init__(self,callid,name,number,time,reason):
        self.id = callid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display(self):
        print self.id
        print self.name
        print self.number
        print self.time
        print self.reason

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0 
    def add(self,callid,name,number,time,reason): 
        self.calls.append(Call(callid,name,number,time,reason))
        self.queue += 1 
    def remove(self):
        self.calls.pop(0)
        self.queue -=1
    def findnumber(self,phone):
        for el in range(0,len(self.calls)):
            if self.calls[el].number == phone:
                self.calls.pop(el)
        self.queue -= 1
    def info(self):
        for el in range(0,len(self.calls)):
            print self.calls[el].id
            print self.calls[el].name
            print self.calls[el].number
            print self.calls[el].time
            print self.calls[el].reason
        print self.queue 
        print "done printing"


center1 = CallCenter() 
center1.add(1,"Jake",1234567,"10:00am","internet down")
center1.add(2,"Jon",1234567,"11:00am","moving")
center1.add(3,"Ron",1234567,"9:00am","hooky")
center1.add(4,"Tom",3234567,"8:00am","won't boot")
center1.info() 
center1.remove()
center1.info()
center1.findnumber(3234567)
center1.info()




