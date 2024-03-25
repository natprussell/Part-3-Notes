class Employee: 
    def __init__(self, firstName, lastName):  #init is short for intialize... Also self is a placeholder that will always be present with __init__ 
        #careful with indentations
        self.firstName= firstName # must include placeholders
        self.lastName=lastName
    def email (self):
        return self.firstName + self.lastName + '@company.com'
    def fullName(self):
        return self.firstName + " "+ self.lastName

empl1= Employee('Grant','Clary')
empl2= Employee('Hillary', "Cliffbar")


print(empl1.lastName) # will print last name only
print(empl1.email())
print(empl1.fullName())

print(empl2.email())
print(empl2.fullName())

