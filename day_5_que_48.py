#input is given as hello123
#output is 6
#sum is sum of digits

#str="hello123"
#d="0123456789"
#sum=0
#for i in str:
    #if i in d:
        #sum+=int(i)
#print(sum)

#sum of digitsof a number using ascii values

inp=input()
sum=0
for i in inp:
    if(ord(i)>=48 and ord(i)<=57):  
         sum+=int(i)
print(sum)