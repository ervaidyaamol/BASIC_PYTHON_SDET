## -aquaring from atributes and behaviuer from one class to another class

## single
class A:
    def m1(self):
        print('this is m1 method  from class A')

class B(A):
    def m2(self):
        print('this is m2 method from class B')

bobj=B()
bobj.m1()
bobj.m2()


## mutilpe inheritance----
# class A:
#     x,y =10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=40,60
#     def m2(self):
#         print(self.a+self.b)
#
# class C(B):
#     i,j=5,4
#     def m3(self):
#         print(self.i+self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


###---hirachy inheritance--
# class A:
#     x,y=10,30
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=20,40
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=200,400
#     def m3(self):
#         print(self.i+self.j)
#
# bobj=B()
# bobj.m1()
# bobj.m2()

# cobj=C()
# cobj.m3()
# cobj.m1()

###
