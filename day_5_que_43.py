#strings is a sequence of charecters
#strings are imutable we cannot modift once it created
#advantage of string 
#methods of string 
#len()
#is lower()
#is upper()
#is alpha()
#is numeric()
#is alnum()
#is digit()
#it return boolean value
#title-->combination of upper case lower case
#swap()-->converting upper to lower and lower to upper
#trim()
#strip()-->leaving and taking spaces
#convert into uppercase
#convert into lowercase
#default input variable input name is input

str=input()
print(len(str))
print(str.islower())
print(str.isupper())
print(str.isalnum())
print(str.isdigit()) #only 0 to 9
print(str.isnumeric())  #all the numners
print(str.isalpha())
print(str.title())
print(str.capitalize())
print(str.strip())
print(str.replace('a','z'))
print(str.split('a'))
print(str.swapcase())
print(str.isascii())  #check wheather the input  is ascii or not
