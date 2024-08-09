#This is a example of for loop
fruit_list =["Apple","Orange","Charry","banana","Halicopter"]

for fruit in fruit_list:
    print(fruit)
    if fruit=="Halicopter":
        print("That is not fruit ")
    elif 'a' in fruit:
        print("That fruit must be yumm")

print("***********************************")

#while loop
count = 0
othercounter = 0
while count < 5:
    print("count :",count)
    count +=1
    othercounter +=1
    print("othercounter :",othercounter)
    othercounter +=1

print("************************************")

for number in range(1,10):
    print(number)

print("*************************************")
for fruit in fruit_list:
    if fruit=='Charry':
        break
    print(fruit)

print("*************************************")

for fruit in fruit_list:
    print(fruit)
    for letter in fruit:
        if 'b' in letter:
            print(letter +" is a yum letter")
        else:
            print(letter +" is a youk letter")

print("***************************************")
string1 ="Ali"
string2 ="ahmadi"
result = string1+' '+string2
print(result)

suffix ="sir"
prefix ="khan"
result= suffix +' '+ string1 +' '+string2 +' '+prefix*3
print(result)

print("*****************************************")

print(result)
print(result[0])
print(result[0:5])
print(result[5:])
print(result[:5])
print(result[::3])
print(result[-20])
print(len(result))
str(444342.3556)
print(string1.upper())
print(result.lower())
print(string2.capitalize())
print(result.upper().lower().capitalize())
print(result.find("sir"))
print(result.replace('khan','mister'))
print(result.split(" "))
print(result.join(fruit_list))
string3=string1.split()
print(string3)

print('***************')

sufix="nona"
for fruit in fruit_list:
    forantfruit = fruit[:3]
    backfruit = fruit[3:]
    z= backfruit+forantfruit
    if 'b' in fruit:
        print(z+sufix)
    else:
        print(z)