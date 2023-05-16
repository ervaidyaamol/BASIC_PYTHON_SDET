# # comditonal_staement
#
# # example 1 - personal is elogibale to vote or not
#
# # age>=18
#
# age=15
# if age >=18:
#     print('voting persona')
#     print("eligible for vote ")
# else:
#     print('not eligible for vote')
#
#
# # example2 -
# if True:
#     print('true condtion')
# else:
#     print('false condtion')
#
#  # eamle-3
# if 1:
#     print("one")
# else:
#     print('not one')
#
# a=10
# {print('haloo'),print('no')}
# if a>=10 else: {print('ho'),print('me')}
#
# num=10
# if num%2==0:
#     print("even")
# else:
#     print('odd')
#
# num=10
# print('even') if num%2==0 else print('odd')
#
# weekno=10
# if weekno==2:
#     print('sunday')
# elif weekno==2:
#     print('monday')
# elif weekno ==3:
#     print('wensday')
# elif weekno== 4:
#     print('thurday')
# else:
#     print('invalid weekno::')

# +ve or _ve number

# num=float(input('enter the number :'))
# if num> 0:
#     print('positive umber')
# elif num<0:
#     print('negative value')
# else:
#     print('invalid input')

# example --larget of 2 number
a=10
b=20

if a>b:
    print('greater')
else:
    print('less than')

# ex- larget of 3 numbers

a=20
b=40
c=50

# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

sunday=1
monday=2
wensday=3

if sunday==2:
    print ('weel')
elif monday==2:
    print('kmm')
else:
    print('not ')