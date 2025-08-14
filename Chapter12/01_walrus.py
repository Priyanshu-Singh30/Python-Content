#Using walrus operator

if(n:= len([1,2,34,4]))>3:
    print(f"List is too long({n} elements, expected <=3)")
    
## Types Defination in python
#variable type function
a:int= 3

#function Type

def sum(a:int,b:int): 
    return a

## Advanced Type Hints

from typing import List, Tuple, Union

