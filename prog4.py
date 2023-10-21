class Circle:
    pi=3.14 #class object Attribute
    def __init__(self,radius=5):
        self.r=radius
        self.area=Circle.pi * self.r*self.r
    def Circumference(self):
        return ('%5.4f' %(2*Circle.pi*self.r))
    
cir1=Circle()
print(cir1.Circumference())
cir2=Circle(16)
print(cir2.Circumference())