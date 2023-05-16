### dictionary ----------------{ keys : value }
## unorderd -----indexed---mutable -----curly brackets-------{ }

### create dictionary-----

dict1 = {"brand": "Ford",
         "model": "Mustang",
         "year": 1964}
dict2 = {'name': 'amol',
         'age': 32,
         'city': 'pune'}
# print(dict1)

# print('lenth of dictionary : ',len(dict1))   ### lenth of dictionary find
#
# print('data type is :  ',type(dict1))   ### data type of dictionary can be find
# print(len(dict1))

### accesing items from dictionary-------
dict1 = {"brand": "Ford",
         "model": "Mustang",
         "year": 1964}
####### method 1-----
# print(dict1['brand'])

#### method 2-------------using ,get()
# x=dict1.get('brand')
# print(x)

#### ---change value in dictionary----

# dict1['year']=2020
# print(dict1)

### reading items form ditionary uising loop---
# 1)

# for i in dict1:
#     print(i)   ### ---print only value from dictionary-
# 2)
# for i in dict1:
#     print(dict1[i])  ### ---print only value from dictionary-

# 3)
# for x,y dict1.items():
#     print(x,y)

### check key is present in dictionary or not----
#
# if 'model' in dict1:
#     print('exits')
# else:
#     print('not exits')

# 2)
#  if ('model' in dict1):

###  ---adding items in dictionary----

# dict1['age']=76
# print(dict1)
#
# dict1['city']='pune'
# print(dict1)

###-- remove items from dictionary-----
### 1) ---------by using pop() ----function

# dict1.pop('age')
# print(dict1)

### 2) ----- by using del function------------

# del dict1      ### it is not perform in my system
# print(dict1)

### 3) -------by using clear() -------function all the keys : values wull be deleted

# dict1.clear()
# print(dict1)   ## ----- display the empty dictionary------

#####------------ copy dictionary -----

#### 1) without using copy function----------

# dict10=dict1
# print(dict10)

####### 2) with .copy()----- funiction will be using--------

dict10=dict1.copy()
print(dict10)