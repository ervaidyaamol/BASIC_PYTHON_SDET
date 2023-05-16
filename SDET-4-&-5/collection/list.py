##  list
orderd and changable
represended---[]
mutable--chagable
sigle variable can store multilpe value


list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']

### count number of times itesms in list-----
list1.count('apple')
print(list1.count('apple'))
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# ## crete list
mylist=[10,29,738,76]
print(mylist)
mylist=['ammple','mango']
mylist2=[]## empty list
print(mylist2)

# ### access items from list
# mylist=['apple','mango','pineapple','banana'] ## idex start from zero- 0 and
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])   ##--negative indexing allowed start from -1

## ex--3 -- range of indexes------

# list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
#
# print(list1[2:4]) ## ['cherry', 'pineapple']
#
# print(list1[-3:-1]) # ['watermelon', 'mango'] ---it will except ( n-1) from list

## ex-4 ---how to chage the items value ---from list ??

# list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
#
# print(list1)
#
# list1[0]='mapple'
# print(list1)
#
# ### ex --5 read the list items using loop
#
# for i in list1:
#     print(i)

## check items in list or not
# list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']
#
# if 'mapple' in list1:
#     print('yes apple is in list1')
# else:
#     print('apple is not prsent in list')



### list lenth
# list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']
# print(len(list1))

# ### add items in list 1--append(''item name),--- 2---insert(index,'item name')
# list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']
# mylist=['maple','rose']
# list1.append(mylist)
# print(list1)
#
# list1.insert(2,'icecream')
# print(list1)

###remove item from list
# list1 = ["apple", "banana", "cherry",'pineapple','kiwi','watermelon','mango','orange']

# print(list1)
# list1.pop(0)
# print(list1)
# list1.pop(-1)
# print(list1)
#

### del()

# list1.clear()
# print(list1)

## copy list into another list
#1---by using = operator
# list10=list1
# print(list10)
# # #2--- by using + operators---
# list4=list1 + list2
# print(list4)
#
# list1=list2.copy()
# print(list1)

### USING LOOP STEEMNT

for i in list2:
    list1.append(i)
print(list1)

### using extend------

list1.extend(list2)
print(list1)


