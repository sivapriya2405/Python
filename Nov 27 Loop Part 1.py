
#Range Function
print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))

#-----------------------------------------------------------------------------

#Task2:

#Get list of strings from user
#separate it in to two lists with vowles and non vowels 

#["hi","ggg","hello","ravi","bbbb","zzz","yyyy"]

#No of elements with vowel: 4
#No of elements without vowel: 3
liststr= []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter the String at List[{0}]".format(i))
    item = (input())
    liststr.append(item)
print("User list is ", liststr)

listv=['a','e','i','o','u']

listvowel=[]
listconsonant=[]

for str in liststr:
    vowel =0
    for char in str:
        if(char in listv):
            vowel=vowel+1
            break
    if(vowel>0):     
        listvowel.append(str)
    else:
        listconsonant.append(str)
        
#print("No of elements with vowel",(listvowel))
#print("No of elements without vowel",(listconsonant))
print("No of elements with vowel",len(listvowel))
print("No of elements without vowel",len(listconsonant))
#----------------------------------------------------------------------------


#Task3:

#Get list of strings from user
#separate it two list (with same first letter and last letter and othr)

#["garg", "kohli", "rohitr", "ishan", "dhoni","dad"]

#No of elements with same first letter and last letter: 3
#Other List: 3
liststr= []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter the String at List[{0}]".format(i))
    item = (input())
    liststr.append(item)
print("User list is ", liststr)
same=0
for str in liststr:
    length=len(str)
    if(str[0]==str[length-1]):
        same=same+1        
print("No of elements with same first letter and last letter",(same))
print("No of Other elements",len(liststr)-same)

#Task4:
#Get a list of numbers from user
#separate it in to even number and odd number (you should create only one empty list)

listnum= []
n = int(input("Enter the list size "))
for i in range(0, n):
    print("Enter the Number at List[{0}]".format(i))
    item = int(input())
    listnum.append(item)
print("User list is ", listnum)
listodd= []
for num in listnum:
    if(num%2!=0):
        listodd.append(num)
        listnum.remove(num)
print("Even number List",(listnum))
print("Odd number List",listodd)
#----------------------------------------------------------------------------
#Task5:
#fibonacci series

#0,1,1,2,3,5,8,13,21,34,55,89,144

#get one input from user: 5

#[0,1,1,2,3]
#3

n = int(input("Enter a Number : "))
a, b = 0, 1
count = 0
while count < n:
       print(a)
       c = a + b
       a = b
       b = c
       count += 1
#---------------------------------------------------------------------------------
#Task6:

#No range function  

#Multiples of 10 between 12 to 100 using while loop
print("Multiples of 10 between 12 to 100")
i=12
while(i<=100):
    if(i%10==0):
        print(i)
    i=i+1
#Multiples of 8 between 120 to 20 using while loop
print("Multiples of 8 between 120 to 20")
i=120
while(i>=20):
    if(i%8==0):
        print(i)
    i=i-1
#Multiples of 5 between 9 to 40 using while loop
print("Multiples of 5 between 9 to 40")
i=9
while(i<=40):
    if(i%5==0):
        print(i)
    i=i+1
#Multiples of 8 between 300 to 200 using while loop
print("Multiples of 8 between 300 to 200")
i=300
while(i>=200):
    if(i%8==0):
        print(i)
    i=i-1

#------------------------------------------------------------------------------
    #Task7:

#print all elements in the list using while loop

#example for loop

#for i in Li1:
    #print(i)
    
#1. calculate len
#2. decrement one by one in while


li=[123, 124, 125,130,131]
i=len(li)-1
while(i>=0):
    print(li[i])
    i=i-1



#------------------------------------------------------------------------------
  

#Task8:

#check whether a number is armstrong or not using while loop
#Dont convert number to string 

number= int(input("Enter the number : "))
length = len(str(number))
val = 0
temp = number
while temp > 0:
   digit = temp % 10
   val+= digit ** length
   temp //= 10
if number == val:
   print("{} is an Armstrong number".format(number))
else:
   print("{} is not an Armstrong number".format(number))

#--------------------------------------------------------------------------------------

#Task9:

#Get one dynamic list from user

#10 [0,6,5,-3,4,5,3,-2,4,0]

#count ==> no of zeros, no of positive values, no of negative values, no of odd numbers, number of even numbers
#print the elements

listnum= []
n = int(input("Enter the list size "))
for i in range(0, n):
    print("Enter the Number at List[{0}]".format(i))
    item = int(input())
    listnum.append(item)
print("User list is ", listnum)
odd,even,positive,negative,zero=0,0,0,0,0
listodd=[]
listeven=[]
listpositive=[]
listnegative=[]
listzero=[]
for num in listnum:
    if(num%2!=0):
        odd=odd+1
        listodd.append(num)
    if(num%2==0):
        even=even+1
        listeven.append(num)
    if(num>0):
        positive=positive+1
        listpositive.append(num)
    if(num<0):
        negative=negative+1
        listnegative.append(num)
    if(num==0):
        zero=zero+1
        listzero.append(num)


print("Number of Zero is : {} and its Elements{}".format(zero,listzero))
print("Number of Odd is : {} and its Elements{}".format(odd,listodd))
print("Number of Even is : {} and its Elements{}".format(even,listeven))
print("Number of positive is : {} and its Elements{}".format(positive,listpositive))
print("Number of negative is : {} and its Elements{}".format(negative,listnegative))
#-----------------------------------------------------------------------------------

#Task10:

#two numbers from user 2 25
#2 
#3  fizz
#4
#15
#16
#25

#multiple of 3 ==> fizz
#multiple of 5 ==> buzz
#multiple of 15 ==> fizzbuzz
#Others ===> No fizz and buzz

#Including last number
#while loop
listnum= []
i = int(input("Enter the First number "))
l = int(input("Enter the Last number "))
while(i<=l):
    if(i%3==0) and(i%5==0):
        print(i," fizzbuzz")
    elif(i%3==0) :
        print(i," fizz")
    elif(i%5==0):
        print(i," buzz")
    else:
        print(i)
    i=i+1

#forloop
    
listnum= []
f = int(input("Enter the First number "))
l = int(input("Enter the Last number "))
for i in range(f, l+1):
    if(i%3==0) and(i%5==0):
        print(i," fizzbuzz")
    elif(i%3==0) :
        print(i," fizz")
    elif(i%5==0):
        print(i," buzz")
    else:
        print(i)
        
