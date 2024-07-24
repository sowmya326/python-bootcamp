##polymorphism method over riding


class Animal:
    def Speak():
        return"speaking.."
class Tiger:
        def Speak():
            return"tiger is speaking"
class Cub:
     def Speak():
          return"cub is speaking"
obj2=Tiger
print(obj2.Speak())    