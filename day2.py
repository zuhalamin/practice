a = 13
b = 19
if a>b :
    print('a is greater than b ')
elif a < b:
    print('b is greater than a')
else:
    print('Welcome')

#Example of if
age = 18
if age >= 18:
    print('you can vote')

#Example of if-else
age = 16
if age>=18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

#Example of if-elif-else
age = input('Enter your age:')
print('Here is you are your result'+age)

age = 18
if age >= 18:
    print('You are eligibal to vote and welcome')
elif age < 18:
    print('You are not elidible to vote,you are kids')
elif age >80:
    print('you can not vote ')
elif age >100:
    print('You are old and you are not eligible')
else:
    print('you have voted before')

#Example of nested if 
x = 14
if x>34:
    print('x is greater ')
    if x <23:
        print('also x greater ')
else:
    print('we can not find same number ')

#boolen expression
x = 5
y = 8
z = 10
print(x==y)
print(x>y)
print(x<y)
print(x==y and z>y)
print((x>3 and y<54)or z ==1)
print('End of boolen expression')

#boolen vribles
is_sunny = True
is_rainy = False
print(is_sunny)

is_weekend = True
if is_weekend:
    print('Enjoy your weekend')
else:
    print('Hard work')

is_sunny = True
is_hot = False
if is_sunny and not is_hot:
    print('It is a good day for walking')



