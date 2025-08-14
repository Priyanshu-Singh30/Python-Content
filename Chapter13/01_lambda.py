# def square(n):
#     return n*n
# print(square(5))

square= lambda x: x*x
print(square(5))

# Topic: Join method

l=["Priyanshu", "Rohit", "Harsh"]
final="--".join(l)
print(final)

#Topic: Format method in python

a="{1} is a good {0}".format("Priyanshu", "boy")
print(a)