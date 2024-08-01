bookstory=['Mat Book','English Book','Dari Book']
print(bookstory)

newlist=["apple","banana","mango","banana","charry","pesch","avacado"]
print(newlist)
print(len(newlist))

list1=['book','pan','papaer']
list2=[1,2,3,4,5]
list3=[True,False,False]
print(list1)
print(list2)
print(list3)

deff=['zuhal',34,'book',True]
print(deff)
print(type(bookstory))
print(newlist[2])
print(newlist[-1])
print(newlist[2:5])
print(newlist[:5])

#change item
bookstory[2]="persion book"
print(bookstory)
newlist[2:5]=["strawberry","pineapple"]
print(newlist)
list1.insert(1,"net")
print(list1)
list2.append(6)
print(list2)

list1.extend(list3)
print(list1)

list1.remove("papaer")
print(list1)

list2.pop(3)
print(list2)

del list3[1]
print(list3)

list4=['yes','no','nothing']
list4.clear()
print(list4)

listt=['phone','computer','TV','taplet']
newlist=[]

for x in listt:
    if "a" in x:
        newlist.append(x)
print(newlist)


num=[4,6,8,90,1,23,8,5]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

list5=listt.copy()
print(list5)

list6=list(listt)
print(list6)

list7=listt[:]
print(list7)

listt=['a','b','c','d']
listt1=[1,2,3,4,5]

listt2=listt+listt1
print(listt2)

listt.extend(listt1)
print(listt)

#tuple
thistuple = ('afg','AU','US','iran')
print(thistuple)
print(len(thistuple))

#one tuple
thistuple1 = ('Afghanistan',)
print(type(thistuple1))

tuple1=(1,2,3,4,5,6,7)
tuple2=('one','two','three','four')
tuple3=('True','True','false')
tuple4=('Book',34,'True',87,'full')
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))

tuple5=tuple(('book','name','pan'))
print(tuple5)

print(tuple1[4])
print(tuple4[2])
print(tuple2[-1])
print(tuple3[1:2])
print(tuple1[1:])
print(tuple2[:3])
print(tuple3[-1:-2])

if "full" in tuple4:
    print('Yes this is existen in tuple')
else:
    print('This is not in tuple ')


tuuple7 = ("book","pen","paper")
list9 = list(tuuple7)
list9[2]="full"
tuuple7= tuple(list9)

print(list9)

a =('book','one','two')
b = list(a)
b.append('pen')
a = tuple(b)

print(a)

c = ('phone',)
a += c
print(a)

print("new ")

d = list(a)
d.remove('book')
a = tuple(b)
print(a)

