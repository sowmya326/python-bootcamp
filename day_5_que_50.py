#print ascii values

#print(ord('A'))
#print(chr(65))
#48-57 is the range of ascii value from 0to 9
#to print all ascii values in single line
#32-47 special char 
for i in range(32,128):
    print(chr(i),end=" ")