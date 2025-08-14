''' Write a prograk to find the maximum of the numbers in a list using the reduce function'''
from functools import reduce
l=[1,34,5,7,876,78,788,54]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))

    