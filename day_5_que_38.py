#input hello-----wor----ld
#output---------hello world

str=input()
for i in str:
    count=0
    ans=""
    for i in str:
        if(i=="-"):
            count+=1
        else:
            ans=ans+i
print("-"*count+ans)


