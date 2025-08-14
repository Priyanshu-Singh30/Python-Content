##Global variable Topic

a=9
def fun():
    global a
    a=2
    print(a)
fun()
print(a)

##Enumerate.py
l=[3,45,6,7]
# index=0
# for i in l:
#     index+=1
#     print(f"the item number {index} is {i} ")

#this can be simplified using enumerate function
for index, item in enumerate(l):
    print(f"the item at index {index} is {item}")