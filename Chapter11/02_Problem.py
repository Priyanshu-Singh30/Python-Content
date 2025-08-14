#Create a class "pets" from a class "animal" and further create a class "Dog"
#from "pets". Add a method "bark" to class "dog"

class Animals:
    pass

class Pets(Animals):
    @staticmethod
    def show():
        print("This is pets class")


class Dog(Pets):
    @staticmethod
    def bark():
        Pets.show()
        print("Bow Bow!")


d=Dog()
d.bark()