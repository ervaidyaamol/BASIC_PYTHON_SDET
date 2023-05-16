# # create string varilables
# s="amol"
# s='amol'
# s=str('amol')

# # @@ceate the empty string
# name=str()
# name=""
# name=''
#

# # # mutable and immutanle
# # mutable---chage the value iof variables
# # immutable-- cannot change the value
#
# # strings are immutable
# str1='welcome'
# print(id((str1)))
#
# str1=str1+'to python'
#
# print(id(str1))

## ex --3 + and * with string
#
# str ='welcome'
#
# print(str+'  welcome')
# print(str * 3)


## ex 4 --slicing
#staring INNDEX- SATRING from 0
# ending index from 1

# str='welcome'
# print(str[1:3])
#
# print(str[:6]) ## by default take 0 as starting index
#
# print(str[2:])## by defacut take all the values from 2 index
#
# print(str[1:-1])


#ex--5
#
# print(ord('a'))  ##returns the ascii code of the chracter
# print(chr(65)) ## returns the chracter represented by a ascii number
#
# ## ex-6 - max() and min() len()
#
# print(max('abc'))
# print(min('abc'))
# print(len('abc'))---#lenght of string

#ex- 7 : ##  in ,not in operators

s='welcome'
#
# print("come" in s)
#
# print('me' in s)
#
# print('wel' in s)
#
# print('wel' not in s)

## ex 8 --- string comparision

# print('time'=='tie')
# print('teeth'> 'tee')
# print('tea'!= 'tea')

## ex- 9 testing strings

s= "welcome to python "
#
# print(s.isalnum())
# print(s.islower())
# print(s.isspace())
# print(s.istitle())
# print(s.isupper())
#
# print("  ".isspace())
# print('273'.isdigit())
#
# print('WELCOME'.isupper())
#

## ex 10 ---searcing for substring from string

s='welcome to python'
# print(s.endswith('thon'))
#
# print(s.find(("come")))
#
# print(s.endswith('n'))
# print(s.startswith('w'))
#
# print(s.title())
#
# print(s.isdigit())
#
# print(s[ : : -1])
# print(s[::-1])

## EX--- convrsion of string

s1=s.capitalize()
print(s1)

s1=s.lower()
print(s1)

s1=s.title()
print(s1)

s1=s.swapcase()
print(s1)

s='welCOME to python'

s1=s.swapcase()
print(s1)

s1=s.replace('on' ,'no')
print(s1)

s1=s.replace('python', 'java')
print(s1)

## ex--- reverse string

# method1
s='welcome'

rev_str=''
for i in s:
    rev_str=i+rev_str

print('reversed string is : ',rev_str)



#method --2

s='welcome'
text=s [::-1]
print(text)