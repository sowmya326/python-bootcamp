#####patterns
#*****
#*****
#*****
#*****
#*****
# outer loop will print row
# inner loop will print coloum

n=int(input())
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()


for i in range(10):
    for j in range (10):
        if(i==j):
            print(" ", end="")
        else:
            print("*", end="")
    print()