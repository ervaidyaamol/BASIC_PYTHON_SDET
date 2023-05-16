class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

### ex -----------
class myclass:
    def __init__(self):
        print('this is constructor')
    def m1(self):
        print('hello')
    def m2(self,x,y):
        return (x+y)

mc=myclass()
mc.m1()

print(mc.m2(10,20))

####-----parametarized constructor-----

# class myclass:
#     name='join'
#     def __init__(self,name):
#         print(name)
#         print(self,name)
#
# mc.myclass('david')


###---------------------------
class emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self,eid,self.ename,self.sal)

m
e1.emp(101,'join',50000)
e1.display

e2=emp(103,'scott',80000)
e2.display()
