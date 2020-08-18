import turtle
a = turtle.Turtle()

def square():
  a.forward(200)
  a.right(90)
  a.forward(200)
  a.right(90)
  a.forward(200)
  a.right(90)
  a.forward(200)

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
year = '2010 , 2012 , 2013  , 2017 , 2019 , 2020 '
print(type(year))
print(year)

l = year.split(" , ")
# c = year.split("2017")
# print(type(l))
# print(l)
# print(c)

  # JOIN
joined = ' this is ' .join(l)
comma = ' , ' .join(l)
print(joined)
print(comma)

