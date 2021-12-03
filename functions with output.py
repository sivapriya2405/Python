#check whether a number is prime or no using functions
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return True
            break
    return False
num=int(input("Enter the number "))
if(isprime(num)):
    print(num ,"is not a prime number")
else:   
    print(num ,"is a prime number")


= RESTART: C:/Users/aarumugam/AppData/Local/Programs/Python/Python310/functions.py
Enter the number 12
12 is not a prime number

= RESTART: C:/Users/aarumugam/AppData/Local/Programs/Python/Python310/functions.py
Enter the number 13
13 is a prime number


#-----------------------------------------------------------------------------

#check whether a number is odd or even using function
def isevenorodd(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("Enter the number "))
if(isevenorodd(num)):
    print(num ,"is a Even number")
else:   
    print(num ,"is a Odd number")

== RESTART: C:/Users/aarumugam/AppData/Local/Programs/Python/Python310/fun.py ==
Enter the number 12
12 is a Even number

== RESTART: C:/Users/aarumugam/AppData/Local/Programs/Python/Python310/fun.py ==
Enter the number 13
13 is a Odd number

#---------------------------------------------------------------------------------
#check whether a number is positive or negative using functions
def ispositive(num):
    if num>0:
        return True
    else:
        return False
num=int(input("Enter the number "))
if(ispositive(num)):
    print(num ,"is a Positive number")
else:   
    print(num ,"is a Negative number")

== RESTART: C:/Users/aarumugam/AppData/Local/Programs/Python/Python310/fun.py ==
Enter the number 2
2 is a Positive number

== RESTART: C:/Users/aarumugam/AppData/Local/Programs/Python/Python310/fun.py ==
Enter the number -5
-5 is a Negative number

#------------------------------------------------------------------------------
#check whether a string is palindrome or no using functions
def isPalindrome(string):
    if string==string[::-1]:
        return True
    else:
        return False
s=(input("Enter the string "))
if(isPalindrome(s)):
    print(s ,"is a Palindrome")
else:   
    print(s ,"is a not a Palindrome")


== RESTART: C:\Users\aarumugam\AppData\Local\Programs\Python\Python310\fun.py ==
Enter the string MOM
MOM is a Palindrome

#----------------------------------------------------------------------------


def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num=int(input(("Enter the number")))
print("Factorial of {} is {}".format(num,factorial(num)))


== RESTART: C:\Users\aarumugam\AppData\Local\Programs\Python\Python310\fun.py ==
Enter the number5
Factorial of 5 is 120
#-------------------------------------------------------------------------------


#Find fibonacci series using functions/recursive function


def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))


num=int(input(("Enter the number")))
for i in range(num):
    print(fibo(i))



== RESTART: C:\Users\aarumugam\AppData\Local\Programs\Python\Python310\fun.py ==
Enter the number5
0
1
1
2
3

