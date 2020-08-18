# import turtle
import re

# a = turtle.Turtle()

# def square():
#   a.forward(200)
#   a.right(90)
#   a.forward(200)
#   a.right(90)
#   a.forward(200)
#   a.right(90)
#   a.forward(200)

# square()
# a.forward(200)
# square()

# import calendar
# print(calendar.weekheader(3))

# print(calendar.firstweekday())
# print()

# print(calendar.month(1980, 12 , w=2))
# print()

# print(calendar.monthcalendar(2019,5))
# print()

# print(calendar.calendar(2020))

# a = calendar.weekday(2020 , 7 , 13)
# print(a)

# leap = calendar.isleap(2020)
# print(leap)

# dino = 1000
# elephant = 100
# if(dino < elephant):
#   square()
# else:
#   a.forward(200)


    # while loop
# muddi = "cool"
# while(muddi == 'cool'):
#   square()

# muddi = "cool"
# while(muddi == 'cool'):
#   square()
    # break

# if True:
#   square()

# for i in range(10):
#   print(i)

# tables = int(input(''))
# for x in range(tables , 10):
#   print(x)

# table = int(input("Enter the number:"))

# for i in range(1, 11):
#    print(table,"X",i,"=",table * i)

# for count in range(4):
#   square()

    # LIST
# l = [1,2,3,4,5]
# print(l)
# names = ['lol' , 'pol' , 'chol' , 'dol']
# print(names)
# names.append('khan')
# print(names)

# names.insert(2, 'khan')
# print(names)
# names.sort()
# print(names)

# for name in names:
#   print(name)

  # SLICING

# num = [1,2,3,4,5,6,7,8,9,10,11]
# print(num[2])
# print(num[-2])
# name = "yoo man"
# print(name[0:3  ])
# print(num[0:5])
# print(num[0:11:2])
# print(num[::-1])
# print(num[0:10:-1])

# for i in range(len(num)):
#   print(num[0:i])
# for i in range(len(num)):
#   print(num[i:i:3])

    # SPLIT
# year = '2010 , 2012 , 2013  , 2017 , 2019 , 2020 '
# print(type(year))
# print(year)

# l = year.split(" , ")
# c = year.split("2017")
# print(type(l))
# print(l)
# print(c)

  # JOIN
# joined = ' this is ' .join(l)
# comma = ' , ' .join(l)
# print(joined)
# print(comma)

  # TUPLES
# a = ('mudassir' , 18 , 'male')
# (name, age ,gendar) = a
# print(name , age ,gendar)

# person1 = ('lol ' , 18 , "male")
# person2 = ('loli' , 19 , "female")
# people = {person1 , person2}

# for name, age , gendar in people:
#   print(name)
#   print(age)
#   print(gendar)
#   print()


# SETS

# a = {'android' , 'ios' }
# a.add('windows')
# print(a)

# l = {1,2,2,2,3,3,3,3,3,4,4,4,4,4,6,6,5 ,'lol' ,'lol '}
# a = set(l)
# print(a)

# l1 = {'python' , 'javascript ', 'java' , 'c++'}
# l2 = {'java' , 'c++' , 'ruby ' , 'django'}
# a = l1.union(l2)
# print(a)

# ll1 = {'python' , 'javascript ', 'java' , 'c++'}
# ll2 = {'java' , 'c++' , 'ruby ' , 'django'}
# b = ll1.difference(ll2)
# print(b)

  # DICTONARIES
# get()
# items()
# keys()
# values()
# pop()
# pooitems()
# clear()

# contacts = {
#   'mull' :{'name' :'muzzamil' , 'number' : 4524555 , 'email' : 'mul@gmail.com'},
#   'jane' : ['jane' , 2323 , 'jane@gmail.com']
# }

# print(contacts["mull  "])
 


# count = {
#   'meow' : 4,
#  'peow' : 7,
#   'lol' : 10
# }

# print(count.items())
# print(count.keys())
# print(count.values())

# print(count)
# count.pop("lol")
# print(count)

# count.popitem()
# print(count)

# count.clear()
# print(count)

#IMMUTABILTY
# tuple
# INT,FLOAT,bool

# MUTABILITY
# list
# DICTONARIES
# ORDERDICT

# a = (1 , 2 , [1,2,3,4])
# print(a)
# a[2][2] = 44
# print(a)



# list comparision

# names = ['mudassir' , 'fahad' , 'obaid' ]
# l = []

# print(l)
# for person in names:
#   l.append(person + ' khan')
# l.sort()
# print(l)


# movies = {'installer' : 8 , 'lolopol' : 7 , 'meownneow' : 15 , 'polotol' : 4}

# l = []

# for rating in movies:
#   if movies[rating] > 5:
#     l.append(rating)

# print(l)


# text = "My Name Is Khan"
# pattern = re.compile('[MKI]')
# result = pattern.search(text)
# print(result)

s = 'Hello from lololo@gmail.com to orya@yahoo.com about the meeting @2PM'
lst = re.findall('\S+@\S+', s)     
print(lst) 