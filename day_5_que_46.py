#prin t the unique character in a string
str=input()
unique=""
for i in str:
    if str.count(i)==1:
        unique+=i 
print(unique)
    