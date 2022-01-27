import math

import random
"""


4,5,8,9,

................Python Program to Add Two Numbers...
.........1.....
a=10
b=20
c=a+b
print(c)
..........2...............

a = int(input("enter first number:"))

b = int(input("enter second number"))

addition = int(a)+int(b)

print("addition of two numbers is", addition)

.......3.................


def add(a,b):
    sum = a+b
    print(sum)
add(10,20)

.................Python Program to Find the Square Root....

a= int(input("enter the number:"))


print(f"{math.sqrt(a):.2f} ")

swap two variables



a= int(input("enter the first number:"))
b= int(input("enter the  second number:"))
a,b = b,a

print(f"a value is {a}, b value is {b}")

print(random.randint(0,100,5))

value = random.randint(1,100)

for ele in value:

#.......Python Program to Check if a Number is Positive, Negative or 0



a= int(input("enter the number:"))

if a == 0:
    print("given number is 0")
elif a>0:
    print("given number is positive")
else:
    print("given number is negitive")


#..........Python Program to Check if a Number is Odd or Even

a= int(input("enter the number:"))

if a%2 == 0:
    print("viven number is even")
else:
    print("given number is odd")
    


#..............Python Program to Check Leap Year..

a= int(input("enter the number:"))

if (a % 4) == 0:
    if (a % 100) == 0:
        if (a % 400) == 0:
            print("given number is leap year")
        else:
            print("given number is not leap year")
    else:
        print("given number is leap year")
else:
    print("given number is not leap year")

# year = int(input("enter the number:"))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} is a leap year".format(year))
#        else:
#            print("{0} is not a leap year".format(year))
#    else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))




#........Python Program to Find the Largest Among Three Numbers

a= int(input("enter the first number :"))
b= int(input("enter the second number :"))
c= int(input("enter the third number :"))

if a>b and a>c:
    print("first number is the largest number")
elif b>a and b>c:
    print("second number is the largest number")
else:
    print("third number is the largest number")
    
    
#.14..........Python Program to Check Prime Number.....

a= int(input("enter the number:"))

if a>1:
    for ele in range(2,a):
        if a%ele == 0:
            print("given number is not a prime number")

        else:
            print("given number is a prime number")
# else:
#     print("given number is a prime number")

"""

#..............Multiplication program

a = int(input("enter the num:"))
b = int(input("enter the range"))

for ele in range(1,b):
    print(f"{a}*{ele} = {a*ele}")
































