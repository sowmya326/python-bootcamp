###mutilevel inheritance
class Animal:
    def Speak():
        return"animal is speaking"
class Dog(Animal):
    def Bark():
        return"Bow"
class Puppy(Dog):
    def Bark():
        return"Bow"
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj1.Speak())
print(obj2.Bark())
print(obj3.Bark())


