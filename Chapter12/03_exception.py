try:
    a=int(input("enter a number"))
    print(a)

except ValueError as v:
    print(v)
except Exception as e:
    print(e)


# Topic: Raising_Exception in python

a1=int(input("enter the number"))
a2=int(input("enter the second error"))

if(a2==0):
    raise ZeroDivisionError("You can not divide by zero")
else:
    print(f"the number a/b is {a1/a2}")