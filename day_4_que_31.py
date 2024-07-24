#*********leap year*********

n=int(input())
if(n%4==0 and n%100!=0):
    print("leap year")
else:
    print("not a leap year")


    #leap year in a given range

    a ,b=list(map(int,input().split()))
    for i in range(2000,2024):
        if n%400==0 or i%100!=0:
            print(i)