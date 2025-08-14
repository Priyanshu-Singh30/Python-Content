''' Write a program to display a/b where a and b are integer s. if b=0, displayinfinite by handing the 'zeroDivisionError'''
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")