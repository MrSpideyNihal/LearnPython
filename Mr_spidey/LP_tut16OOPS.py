# class abc:
#     a = 10
#     print(10)

# obj = abc()

# print("HELLO")

# class printname:
#     def givename(self,name):
#         print(name)

# obj1 = printname()
# obj1.givename('hello')

# class neww:
#      def __init__(self,a,b):
#         self.a=a
#         self.b=b
#      def add(self):
#         print(self.a+self.b)
#      def mul(self):
#         print(self.a*self.b)
#      def div(self):
#         print(self.a/self.b)
# obj11 = neww(5,3)
# obj11.add()
# obj11.mul()
# obj11.div()

# class Vehicle:
#     def __init__(self,speed,V_model,V_Name):
#         self.speed=speed
#         self.V_model=V_model
#         self.V_Name=V_Name                    
#     def printdetails(self):
#         print("VEHICLE NAME ",self.V_Name)
#         print("VEHICLE MODLE ",self.V_model)
#         print("VEHICLE SPEED ",self.speed)

# newbike = Vehicle(50,"MARUTI","BROOM")
# newbike.printdetails()
# class neww:
#     def __init__(self,r):
#         self.r=r
    
#     def aoc(self):
#         print(3.14*self.r**2)
# obj11 = neww(3)
# obj11.aoc()

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#inheritance
class parentsfather:
    def property():
        print("PROPERTY TRANSFERED")
class parent(parentsfather):
    def fun(self):
        print("hello")
class child(parent):
    def run(self):
        print("bye")
class child111(parent):
    def run(self):
        print("byeeeeeee")


a = child()
a.fun()