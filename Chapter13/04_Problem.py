''' Write a program to filter a kist of the numbers which are divisible by 5'''

def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[1,2,34,556,66,555]
f=list(filter(divisible5,a))
print(f)