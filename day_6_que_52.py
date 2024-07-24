### mutiple inheritance
class Father:
    def father_speak():
        return"father class"
class Mother:
    def mother_speak():
        return"mother speak"
class Kid(Father ,Mother):
    def kid_speak():
        return "im kid ,imhaving all properties of mother and father class"
obj1=Kid
print(obj1.father_speak())
print(obj1.mother_speak())
print(obj1.kid_speak())

