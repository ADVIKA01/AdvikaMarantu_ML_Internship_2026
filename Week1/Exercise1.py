ODE:
#area of rectangle 
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
area=length * breadth
print("Area of rectangle =", area)
#simple intrest
p=float(input("Enter principal:"))
r=float(input("Enter rate:"))
t=float(input("Enter time:"))
si=(p * r * t) / 100
print("Simple Interest=", si)
#celsius to fahrenheit
c=float(input("Enter temperature in Celsius:"))
f=(c * 9/5) + 32
print("Temperature in Fahrenheit=", f)
#average of 3 numbers
a=float(input("Enter first value:"))
b=float(input("Enter second value:"))
c=float(input("Enter third value:"))
avg=(a+b+c)/3
print("Average=",avg)
#square and cube
number=float(input("Enter a number:"))
square=number** 2
cube=number** 3
print("Square=",square)
print("Cube=",cube)
#swap numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a=", a)
print("b=", b)
#student report
name=input("Enter student name:")
roll=input("Enter roll number:")
m1=float(input("Enter marks of subject 1:"))
m2=float(input("Enter marks of subject 2:"))
m3=float(input("Enter marks of subject 3:"))
m4=float(input("Enter marks of subject 4:"))
m5=float(input("Enter marks of subject 5:"))
total = m1+m2+m3+m4+m5
percentage = total / 5
print("\n Student Report")
print("Name:", name)
print("Roll No:", roll)
print("Total Marks:", total)
print("Percentage:", percentage)

OUTPUT:
Enter length:8
Enter breadth:7
Area of rectangle = 56.0
Enter principal:500
Enter rate:3
Enter time:2
Simple Interest= 30.0
Enter temperature in Celsius:48
Temperature in Fahrenheit= 118.4
Enter first value:67
Enter second value:45
Enter third value:73
Average= 61.666666666666664
Enter a number:5
Square= 25.0
Cube= 125.0
Enter first number:6
Enter second number:7
After swapping:
a= 7
b= 6
Enter student name:advika
Enter roll number:11
Enter marks of subject 1:68
Enter marks of subject 2:79
Enter marks of subject 3:87
Enter marks of subject 4:75
Enter marks of subject 5:85

 Student Report
Name: advika
Roll No: 11
Total Marks: 394.0
Percentage: 78.8
