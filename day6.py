def sum(x,y):
    p=x+y
    print(p)

n1=3
n2=6
sum(n1,n2)

print("*************************")

def sum(x,y):
    z=x+y
    print(z)

x1=int(input("Enter your naumber :"))
x2=int(input("enter your second number :"))
sum(x1,x2)

#function from w3school
def my_function(fname):
    print(fname + "ahmadi")

my_function("ali ")
my_function("khan ")
my_function("ahmad ")

print("**************************")

def My_function(name,age):
    print(name+' '+age)

My_function("zuhal","23")

print("****************************")

def my_Function(*student):
    print("Intellgent student of school :"+ student[3])

my_Function("sara","ali","mohamad","rokhsar","jon")

print('******************************')

#keyword argument
def MY_function(kids4,kids3,kids2,kids1):
    print("The yungest kids is :"+ kids1)
MY_function(kids1="ali",kids2="sara",kids3="jon",kids4="khan")

#arbitrary keyword argument
def my_Function1(**family):
    print("bigest member of my family is my :" + family["dad"])
    print("smalest member of my family is :" + family["fourthchild"])
my_Function1(thirdchild="jon",secondchild="ali",fourthchild="sara",firstchild="marya",mom="mom",dad="dad")

def my_function2(country="afghanistan"):
    print("I am from " +country)
my_function2()
my_function2("Australi")
my_function2("Norway")
my_function2("Indea")

#passing a list as a argument

def my_function3(fruit_list):
    for fruit in fruit_list:
        print(fruit)
fruit_list=["aplle","banana","mango","charry"]
my_function3(fruit_list)

#return
def my_function4(x):
    return x * 3
print(my_function4(4))

#Or
def my_function5(y):
    return 5 * y

print(my_function5(4))
print(my_function5(3))

def my_function6(num1,num2):
    sum=num1+num2
    return sum
result=my_function6(4,5)
print("sum of number is :" ,result)

#pass 
def my_function():
    pass

#positional argument
def my_function7(x ,/):
    print(x)
my_function7(4) 

def my_function8(x):
    print(x)
my_function8(x = 9)

def great(name,age):
    print(f"My name is {name} and my age is {age}") #f  string allow us to format selects part of string

great("Zuhal",23)

#keyword parameter
def greet(name,age):
    print(f"My name is {name} and my age is {age}")

greet(age = 24,name="sara")

def my_fun(x,y,/,*,z,a):
    print(x+y+z+a)
my_fun(4,5,z=4,a=6)


                 
