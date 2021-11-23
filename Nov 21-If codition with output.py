
#collect one number from user, check whether the number is positive or negative
a=int(input("Enter the Number: "))
if(a>0):
    print("Given Number '{}' is Positive".format(a))
else:
    print("Given Number '{}' is Negative".format(a))
print()

#output
=================== RESTART: C:\Python\Nov 21-If codition.py ===================
Enter the Number: 100
Given Number '100' is Positive

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#collect one number from user, check whether the number is even or odd
a=int(input("Enter the Number: "))
if(a%2==0):
    print("Given Number '{}' is Even".format(a))
else:
    print("Given Number '{}' is odd".format(a))
print()

#output
=================== RESTART: C:\Python\Nov 21-If codition.py ===================
Enter the Number: 51
Given Number '51' is odd

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#collect one string from user, check whether the string is palindrome 

a=input("Enter the String: ")
rs=a[::-1]
if(a==rs):
    print("Given String '{}' is palindrome".format(a))
else:
    print("Given string '{}' is not a palindrome".format(a))
print()

#output
=================== RESTART: C:\Python\Nov 21-If codition.py ===================
Enter the String: Madam
Given string 'Madam' is not a palindrome
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Get one string from user
#extract middle letter of the string
#check whether middle letter is vowel or no

a=input("Enter the String: ")
ml=int(len(a)/2)
vl=['a', 'e' ,'i' ,'o' ,'u']
if(a[ml] in vl):
    print("Middle Letter of the String '{}' is '{}',It is a Vowel".format(a,a[ml]))
else:
    print("Middle Letter of the string '{}' is '{}',It is not a Vowel".format(a,a[ml]))

print()

#output
=================== RESTART: C:\Python\Nov 21-If codition.py ===================
Enter the String: Welcome
Middle Letter of the string 'Welcome' is 'c',It is not a Vowel

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Get one string from user
#Find the middle letter
#find ascii value for the middle letter
#check whether ascii value is odd or even

a=input("Enter the String: ")
ml=int(len(a)/2)
vl=['a', 'e' ,'i' ,'o' ,'u']
if(ord(a[ml])%2==0):
    print("Middle Letter of the String '{}' is '{}',Its ASCII value {} is even".format(a,a[ml],ord(a[ml])))
else:
    print("Middle Letter of the string '{}' is '{}',Its ASCII value {} is odd".format(a,a[ml],ord(a[ml])))

print()
#output
=================== RESTART: C:\Python\Nov 21-If codition.py ===================

Enter the String: welcome
Middle Letter of the string 'welcome' is 'c',Its ASCII value 99 is odd
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#get one string from user
#check whether length of the string is odd or even


a=input("Enter the String: ")
ml=int(len(a))
if(ml%2==0):
    print("Length of the String '{}':{},It is Even".format(a,ml))
else:
    print("Length of the string '{}':{},It is Odd".format(a,ml ))

print()
#output
=================== RESTART: C:\Python\Nov 21-If codition.py ===================
Enter the Number: 
Enter the String: Welcome
Length of the string 'Welcome':7,It is Odd

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Get one mark from student
#mark 0 to 100 otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A  ==> Even + Odd -
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E

#0 to 49 ===> FAIL

mark=int(input("Enter the Marks : "))
if mark>0 and mark<=100:
    print("Valid Mark")
    if mark>=50:
        print("Pass Mark")
        if mark>=90 and mark%2==0:
            print("A+")
        elif mark>=90 and mark%2!=0:
            print("A-")
        elif mark>=80 and mark%2==0:
            print("B+")
        elif mark>=80 and mark%2!=0:
            print("B-")
        elif mark>=70 and mark%2==0:
            print("C+")
        elif mark>=70 and mark%2!=0:
            print("C-")
        elif mark>=60 and mark%2==0:
            print("D+")
        elif mark>=60 and mark%2!=0:
            print("D-")
        elif mark>=50 and mark%2==0:
            print("E+")
        elif mark>=50 and mark%2!=0:
            print("E-")
    else:
        print("Fail Mark")
else:
    print("InValid Mark")


#output

Enter the Marks : 90
Valid Mark
Pass Mark
A+

========================== RESTART: C:/Python/marks.py =========================
Enter the Marks : 85
Valid Mark
Pass Mark
B-

========================== RESTART: C:/Python/marks.py =========================
Enter the Marks : 65
Valid Mark
Pass Mark
D-

========================== RESTART: C:/Python/marks.py =========================
Enter the Marks : 58
Valid Mark
Pass Mark
E+

========================== RESTART: C:/Python/marks.py =========================
Enter the Marks : 40
Valid Mark
Fail Mark


========================== RESTART: C:/Python/marks.py =========================
Enter the Marks : 120
InValid Mark
