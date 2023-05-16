## tuple---------------------------
#-----ordered and unchagable
# ---represented ---- ()
#----immutable
#---- more secure than list--

### create tuple----
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
tuple2=()
tuple3=''
# print(tuple3)
# print(tuple2)
# print(tuple1)

## acces tuple by using index

# print(tuple1[1])
# print(tuple1[-3:-1])    ###----- # [satring index : and ending index]

##reading tuple items using loop staemnt

# for i in tuple1:
#     print(i)

## changing the tuple items---but u can not chage directly but convert into list and the change it

tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
         ### covert into list then change into list and then print
# tuple1=list(tuple1)
# print(tuple1)
# tuple1[4]='merry'
#
# print(tuple1)

####------ reading tuple items using loop----

# for i in tuple1:
#     print(i)

#####--- searching of items in tuple----
#
# if 'cherry' in tuple1:
#     print('yes , cherry  is prsent in tuple1 ')
# else:
#     print('no cherry is present in tulpe1 ')

####--- tuple lenth or count the number of items in tuple-----
#
# tupleof =len(tuple1)
# print(tupleof)
# print(len(tuple1))

####----- copy tuple into another tuple----------

# tuple10=tuple1
# print(tuple10)


### ----removing tuple item is not possible due to immutable nature ------


### ---- join or combine tuple-----or can called as concatination of 2 tuples----

tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
tuple2= (10,29,43,45,67,89,70,35,98)

# tuple3=tuple1+tuple2
#
# print(tuple3)

####-----  compare the tuple are equal or not ----

# tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
# tuple2= (10,29,43,45,67,89,70,35,98)
# tuple2 = ("apple", "banana", "cherry", "apple", "cherry")

# if tuple1==tuple2:
#     print('tuple is same ')
# else:
#     print('tuple is not same')

#####------
