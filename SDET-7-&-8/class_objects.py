'''class -----collection of variables and methods
                it is logical entity
                does not occupy space in memory
    objects-----
               it is an instance of class
               physical entity
               occupy space in memory

 for one class we can create multiple objects,& objects are independet

 functions---can create without class
 method---create inside the class
 '''

## ex--
# class myclass:
#     def myfun(self):
#         pass
#     def display(self):
#         print('join')
#
# mc1=myclass()
# #mc1=myclass()
# mc1.myfun()
# mc1.display()

##  EX--------
# class myclass:
#     def m1(self):
#         print('this is instance method')
#     def m2(self):
#         print(self,'num')
#
# mc=myclass()
# mc.m1()
# mc.m2(10,10)


'''
    there are 2 type of method we can define with in class
    1)--- instance method--(we can call only through objects)
    2)--- static method---(we can directly call using class )
'''

''''' ex- 1) --global variables-----
          2)-- class variables---
          3)--- local variables'''

# class myclass:
#     a,b=20,30               ## --class variables
#     def add(self):
#         print(self.a,self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=myclass()
# mc.add()
# mc.mul()

####------------------------------
# a,b=15,35
# class myclass:
#     a,b=10,20
#     def add(self,a,b):
#         print(a+b)
#         # print(self.a+self.b)
        # print(globals()['a']+globals()['b'])

# mc=myclass()
# mc.add(100,200)

##-----one class have multiple objects-------

# class myclass:
#     def display(self,name):
#         print("my name is ")
#         print(name)
    # def add(self,name,age,city):
    #     return name,age,city

# mc=myclass
# mc.add('amol',34,'parbhani','pune')
# obj1=myclass()
# obj1.display('join')
# obj2=myclass()
# obj2.display('join')

###---6) ONE class have multiple objects--------
class myclass:
    def display(self,name):
        print('this is display method')
        print(name)

amol=myclass()
amol.display("join")

amol2=myclass()
amol2.display("joni")



