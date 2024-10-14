"""class student:
    name = "Benz"
s1 = student()
print(s1.name)"""

class truck:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
        print("this is a constructor")
    
    def veh_det(self):
        print(t1.color,t1.brand)
t1 = truck("Blue","VT")
t1.veh_det()

