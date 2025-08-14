''' store the multiplication tables geenrated in problem 3 in a file named Tables.txt'''

n=int(input("enter the number:"))

table=[n*i for i in range(1,11)]
print(table)

with open("tables.txt","w") as f:
    f.write(f"Table of {n}: {str(table)}\n")
