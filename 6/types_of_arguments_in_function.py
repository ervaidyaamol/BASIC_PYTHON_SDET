##-1) postional arguments
## 2) keyword arguments

def func(i,j):
    print(i,j)

func(10,20)   ##---postional arguments

func(j=20,i=10) ## keywords arguments

###---------
def func(i,j=10):
    print(i,j)

func(100,200)
func(100)

###------ex-keyword arguments------
def greeting(name,grreting):
    print(grreting+ " "+name)

greeting(name='join',grreting='hello')

## ---
def my_fun(a,b,c):
    print(a,b,c)

my_fun(10,20,30)
# print(10,20,30)
my_fun(10,b=40,c=90)
my_fun(a=30,50,80)   ### ----- SyntaxError: positional argument follows keyword argument