''' Write a program to input name , marks and phone number of a student and format it using the format function like below'''

a=input("enter your name")
b=int(input("enter the marks"))
c=int(input("enter the phone number"))
s="My name is {}, and marks {}, and {}".format(a,b,c)
print(s)