#Convert the given value into other data types
f=float(input("Enter the Float value : "))
print("Integer Value :",int(f))
print("string Value :",str(f))
print("Boolean Value :",bool(f))
print()
i=int(input("Enter the integer value : "))
print("Float Value :",float(i))
print("string Value :",str(i))
print("Boolean Value :",bool(i))
print()
b=float(input("Enter the boolean value : "))
print("Integer Value :",int(b))
print("string Value :",str(b))
print("Float Value :",float(b))
print()
s=float(input("Enter the string value : "))
print("Integer Value :",int(s))
print("Float Value :",str(s))
print("Boolean Value :",bool(s))
print()

#Get Radius (int) and Height(float),Find the area of Cylinder Pi r*r h


r=int(input("Enter the Radius : "))
h=float(input("Enter the Height  : "))
pi=3.14
P=pi*r**2*h
print("Area of the cylinder for the given Radius {} and Height {} is : {} ".format(r,h,int(P)))
print()

#Get Radius (int) ,Find the area (pi r*r)and circumstance (2 pi r)of circle

r=int(input("Enter the Radius : "))
pi=3.14
Area=pi*r**2
Circumstance=2*pi*r
print("Area of the circle for the given Radius {} is : {} ".format(r,int(Area)))
print("Circumstance of the circle for the given Radius {} is : {} ".format(r,Circumstance))
print()
