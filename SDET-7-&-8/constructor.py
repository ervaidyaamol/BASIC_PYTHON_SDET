# constructor------

# class myclass:
#     def __init__(self):
#         print("this is construcotor")
#     def m1(self):
#         print('hello')
#     def m2(self,x,y):
#         print(x+y)

# mc=myclass()   ## invoked construtor atumoatically
# mc.m1()
# mc.m2(10,20)

##3-----parameterized construtor---

# class myclass:
#     # name='join'
#     def __init__(self,name):
#         print(name)
#         # print(self.name)
#
# mc=myclass('amol')

### ---

# class Emp:
#     def __init__(self,eid,name,sal):
#         self.eid=eid
#         self.name=name
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.name,self.sal)
#
# e1=Emp(100,'amol',45345)
#
# e1.display()

###-----
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def __str__(self):
        return (self.ename)

e1=Emp(101,'hoin',50909)
print(e1)


