import random 
class Hospital(object):
    def __init__(self,name,capacity):
        self.patients = []
        self.name = name 
        self.capacity = capacity
        self.beds = []
        for num in range(0,capacity):
            self.beds.append(num)
    def admit(self,idnum,name,allergies):
        if len(self.beds) == 0:
            print "Hospital is full"
        else: 
            newpatient = Patient(idnum,name,allergies)
            newbed = random.randint(0,len(self.beds) - 1)
            newpatient.bednum = self.beds(newbed)
            self.beds.pop(newbed)
            self.patients.append(newpatient)
    def discharge(self,disch):
        for el in range(0,len(self.patients)):
            if self.patients[el].idnum == disch:
                self.patients.pop(el)
                self.beds.append(len(self.beds))
                # There is a chance that I will get overlapping bed numbers. would have to add a check to see if i already have that bed number for larger hospitals
    def checkcap(self):
        print len(self.beds)
        print self.beds
    def patientInfo(self): 
        for el in range(0,len(self.patients)):
            print self.patients[el].idnum
            print self.patients[el].name
            print self.patients[el].allergies
            print self.patients[el].bednum

class Patient(object):
    def __init__(self,idnum,name,allergies):
        self.idnum = idnum
        self.name = name
        self.allergies = allergies
        self.bednum = 0

# Create a hospital called K Hospital
khos = Hospital("K",5)
khos.checkcap()
khos.admit(245,"Alex","nuts")
khos.admit(978,"James","peaches")
khos.admit(482,"Jacob","none")
khos.checkcap()
khos.discharge(482)
khos.checkcap()

