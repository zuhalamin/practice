x = 5 
y = "jone"
print(x)
print(y)

a = int(4)
b = str(6)
c = float(9)
print(a)
print(b)
print(c)

a = 5
b = "zuhal"
c = 9.5
print(type(a))
print(type(b))
print(type(c))

x , y , z = "apple" , "banana" , "mango"
print(x,y,z)
x=y=z="orange"
print(x)
print(y)
print(z)

name = {"abo","zuhal","ayesha"}
z,x,c= name
print(z)
print(x)
print(c)

x = "best book"
def myfunc():
    global x
    x = "a book "
    print("This is the "+x)
myfunc()
print('This is the '+x)

x =3
y =3.5
z =4J
a=int(x)
b=float(y)
z=complex(z)
print(a)
print(b)
print(z)
print(type(a))
print(type(b))
print(type(z))

x = 'banana'
for x in 'banana':
    print(x)

x = 'Helow world this is me !'
print(len(x))
print( 'this' in x)
if 'this' in x:
    print("yes,'this is in the text")

print('this' not in x)

b = "this,books!"
print(b[2:4])
print(b[:11])
print(b[2:])

my_exm= 'We are so happey'
print(my_exm.lower())
print(my_exm.upper())
print(my_exm.replace("W","h"))

#arithmatic operater
x = 5
y = 7
print(x+y)
print(x-y)
print(x/y)
print(x*y)
print(x**y)
print(x//y)
print(x%y)

x +=3
x -=4
x /=6
print(x)

print(x==y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x!=y)
print("other operation")

x =9
print(x >8 and x <21)
print(x >34 or x <24)
print(not(x >34 and y<3))

#if

x =56
y =56
if x>y:
    print('x is greter than y')
elif x<y:
    print('y is greater than x')
elif x==y:
    print('These two latter is same')
else:
    print('nothing')

x = 3
y = 5
z = 8
if x>y and z>y:
    print('this ia true')
else:
    print('something wrong')

if x<y or z<y:
    print('This is true ')

if not x>y:
    print('this is not working ')

if x < y:
    pass

#loop
'''
i = 1
while i < 6:
  print(i)
  if (i==3):
      break
  i += 1
'''
#x = 5
#while x==5:
 #   print('hello')
  #
  # 
  #   x=int(input('Guess what x needs to be!'))

keepgoing=True
while keepgoing:
    choice=input('Do you want to keep going?y/n')
    if choice =='n':
        keepgoing=False
    else:
        print('Okey,Keepgoing ..')
        keepgoing=True
 

 