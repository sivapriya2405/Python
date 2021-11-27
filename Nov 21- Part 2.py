#---------------------------------------------------------------------------------
#Task10:
#two strings from user

#mathematics ===> 4 vowels
#science ==> 3 vowels

#both are equal count or not equal

f=input("Enter the First String : ")
s=input("Enter the Second String : ")

lv=['a','e','i','o','u']
countf=0
counts=0
for char in f:
    if(char in lv):
        countf=countf+1;

for char in s:
    if(char in lv):
        counts=counts+1;

print()
print("First string '{}' contains {} vowels".format(f,countf))
print("Second string '{}' contains {} vowels".format(s,counts))

if(countf==counts):
    print("Both vowel count are equal")
else:
    print("Both vowel count are not equal")

#output
    
======================= RESTART: C:/Python/checkvowel.py =======================
Enter the First String : welcome
Enter the Second String : python

First string 'welcome' contains 3 vowels
Second string 'python' contains 1 vowels
Both vowel count are not equal

#----------------------------------------------------------------------------
#Task11:

#get one integer from user (3 digit int only)
#armstrong or no (without using loops)

#153 ===> 1^3 + 5^3 + 3^3
#370 ===> 3^3 + 7^3 + 0^3
#371 ====> 3^3 + 7^3 + 1^3
def  getSum (num):
    if num==0:
        return num
    else:
        return pow((num%10), order) + getSum(num//10)
num=int(input ("Enter a number :"))
order=len(str(num))
sum=getSum(num)
if sum==(num):
    print("{} is an Armstrong Number.".format(num))
else:
    print("{} is not a Armstrong Number.".format(num))


#output :
    
================= RESTART: C:/Python/Armstrong without loop.py =================
Enter a number :370
370 is an Armstrong Number.

================= RESTART: C:/Python/Armstrong without loop.py =================
Enter a number :153
153 is an Armstrong Number.

================= RESTART: C:/Python/Armstrong without loop.py =================
Enter a number :371
371 is an Armstrong Number.

================= RESTART: C:/Python/Armstrong without loop.py =================
Enter a number :372
372 is not a Armstrong Number.



#------------------------------------------------------------------------------


#length of list odd or even

List =[123, 124, 125,130,131]
if(len(List)%2==0):
    print("Length of the given List is Even")
else:
    print("Length of the given List is Odd")


===================== RESTART: C:/Python/Lentgth of List.py ====================
Length of the given List is Odd

