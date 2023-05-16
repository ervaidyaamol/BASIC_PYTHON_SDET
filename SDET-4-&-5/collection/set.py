#### set---------------
## ---unorderd ---- unindexed---mutable---- curly brackets---- { }
###  ----Create an Empty Set in Python
# set1 = {112, 114, 116, 118, 115}
# set2 = {'Hello', 101, -2, 'Bye'}
# set3 = {'Lacoste', 'Ralph Lauren'}
# set4 = {}
# set1={}
# print(set4)

### -----accessing items from set-------
# for i in set1:
#     print(i)

###---value exits in set or not -----------
    ## method 1----
# if 112 in set1:
#     print('yes it is true')
# else:
#     print('it is wrong')
     ## method 2----

# print('yes it is ',112 in set1)

####--- adding items to set ---- due to set is mutable or changable----

# set1 = {112, 114, 116, 118, 115}
# set2 = {'Hello', 101, -2, 'Bye'}
# set3 = {'Lacoste', 'Ralph Lauren'}
# set4 = {}
        ###---add ----single item in set use ---.add()
#
# set1.add(123)
# set2.add('hi')
# print(set1)
# print(set2)

        ### ---update---multiple items
# print(set1)
# set1.update([100,'amol',144])
# print(set1)

##---------find number of items in list----

# set1 = {112, 114, 116, 118, 115}
# set2 = {'Hello', 101, -2, 'Bye'}
# set3 = {'Lacoste', 'Ralph Lauren'}
# set4 = {}

# set_1=len(set1)
# print(set_1)
     ### or -----

# print(len(set1))

#####-------remove items in set
        ##--remove ---and ---discard
# set1.remove(112)
# set1.remove(112) ## ---single item can remove
# print(set1)

#set1.discard(114)  ##### remove single item value from set
# print(set1)

###------clear all items from set

# set1.clear()  ### ---only set items or value in set delete not delete the set name ,that is empty set will be dispaly

# print(set1)
######--------------del functions for set------

set1= {112, 114, 116, 118, 115}
print(set1)
set2= {'Hello', 101, -2, 'Bye'}
set3= {'Lacoste', 'Ralph Lauren'}
set4= {}

# del set2  ## not execute in my application
# print(set2)


####----join or combine two or more sets----for can not use concatination operation-----

#set5=set1+set2+set3+set4 ## -----can not perform cancatination for set

set5=set1.union(set2)  ####### for multiple add 2 sets
print(set5)

####---------update() function in set

set1.update(set2)
print(set1)

