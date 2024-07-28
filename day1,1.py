#veribale 
x = 5 
y = 23
print(x+y)

x = 34
y = 'book'
print(x)
print(y)

x , y , z = 'blue','red','green'
print(x,y,z) 
print(x)
print(y)
print(z)

a = b = d = 'computer'
print(a,b,d)

frutis = ["orenge","apple","banana"]
x , y , z = frutis
print(x)
print(z)
print(y)
print(x,y,z)
 
d = 'This'
b = 'is'
p = 'wonderful'
print(d,b,p)
print(d+b+p)

s = "sweet"

def myfun():
    global m
    m ='english'
    print(m , s)
myfun()
print(s,m)
 
name = (input('enter your name '))
print('Here is your name:'+name)
age = (input('How old are you:'))
print('Here is your age'+age)
color =(input('what is your favorite?:'))
print('Here is your favorite color:')
