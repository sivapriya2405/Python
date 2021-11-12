#collect one string from user (input)
#identify middle letter of the string


s=input("Enter the string ")
i=int(len(s)/2) 
if(len(s)%2!=0):
 print(s[i])
else:     
 print(s[i-1]+s[i])

# Task 2 : concat with alternative string length
 
a=input("Enter the First string ")
b=input("Enter the Second string ")

print("{}{}{}{}".format(a,len(b),b,len(a)))


#task 3:convert middle character to upper case


s=input("Enter the string ")
i=int(len(s)/2)
print(s[:i]+s[i].upper()+s[i+1:])
