l=[1,2,3,4,5]

# square= lambda x: x*x
# sqList=map(square,l)
# print(list(sqList))

# Filter example

# def even(n):
#     if(n%2==0):
#         return True
#     return False
# onlyEven= filter(even,l)
# print(list(onlyEven))


#Reduce Example

from functools import reduce
l=[1,2,3,4,5]
def sum(a,b):
    return a+b
print(reduce(sum,l))
    

