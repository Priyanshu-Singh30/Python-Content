''' write a program t print third and seventh element from a list using enumerate function.'''

l=[1,3,4,6,7,8,3,4,5,6]
for i, item in enumerate(l):
    if(i==2 or i==4 or i==6):
        print(item)