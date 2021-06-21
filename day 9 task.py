# # 1. fibonacci sequence
n1=0
n2=1
h=int(input("enter how many sequence u need : "))
print(n1)
print(n2)

for i in range(2,h):
    sum= n1+n2
    print(sum)
    n1=n2
    n2=sum
# --------------------------------------------------------------------------

# 2.armstrong number

n=int(input("enter a number : "))
sum=0
temp=n

while temp > 0:
    r= temp % 10
    sum=sum+r**3
    temp//=10

if n == sum:
    print("you're given number is armstrong number")
else:
    print("Sorry you're given number is not a armstrong number")


# --------------------------------------------------------------------------


# 3.multiplication table 9

for i in range(9,10):
    for j in range(0,11):
        print("{0} times {1} is {2}".format(j,i,i*j))

# --------------------------------------------------------------------------


# 4.check positive or negative

num=int(input("enter number"))
if num>0:
    print("its positive")
else:
    print("its negative")

# --------------------------------------------------------------------------

# 5.loop through th list of number

list1=[1,2,3,4,5,6,7,8,9,10]
k=2
list2=[x+k for x in list1]
print("the list after addition is {0}".format(list2))

# --------------------------------------------------------------------------

# 6.pattern program

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")

# --------------------------------------------------------------------------
# 7.days to age

day=int(input("number of days : "))
year = int(day/365)
week =int((day%365)/7)
days=abs((day-(year*365)+(week)))
print("years =",year)
print("days =",days)


# --------------------------------------------------------------------------

# 8.Solve Trigonometry problem using math function write a program to solve using math function

import math
a=math.pi/6
print("value of sin pi/6 is : ",end="")
print(math.sin(a))
print("value of cos pi/6 is : ",end="")
print(math.cos(a))


# --------------------------------------------------------------------------


# 9.	Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
choice=int(input("Enter Choice(1-4): "))

if choice==1:
    a=int(input("Enter value 1:"))
    b=int(input("Enter value 2:"))
    c=a+b
    print("Sum = ",c)
elif choice==2:
    a = int(input("Enter value 1:"))
    b = int(input("Enter value 2:"))
    c=a-b
    print("Difference = ",c)
elif  choice==3:
    a = int(input("Enter value 1:"))
    b = int(input("Enter value 2:"))
    c=a*b
    print("Product = ",c)
elif choice==4:
    a = int(input("Enter value 1:"))
    b = int(input("Enter value 2:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
