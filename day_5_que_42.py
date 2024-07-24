
n=int(input())
for i in range(row):
    print(""*(row-i-1)+ "*" *row)
    for i in range(rows-2,-1,-1):
        print(""*(row-i-1)+"*"*row)
