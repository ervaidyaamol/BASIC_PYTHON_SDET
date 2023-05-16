# global_var=20
#
# def fin():
#     loc_var=30
#     print(loc_var)
#     print(global_var)
#
# fin()
########--------------------------------------------
# xy=100
#
# def cool():
#     xy=200
#     print(xy)
#
# cool()

####---------------------

# xy=100

# def cool():
#     xy=200
#     global xy
#     print(xy)
#
# cool()

######-----------
x=100
def cool():
    global x
    x=300
    print(x)

cool()

print(x)

######-----------------------------------

def cool():
    global x
    x=100
    print(x)

cool()
print(x)

####----------------------
