## print the element in particular index

a=list(map(int,input().split()))
k=len(a)
l=len(a)
for i in range(1,1):
    if(l<k):
        i=k%l
        print(a[k])
        break

    a=list(map(int,input().split()))
    k=int(input())
    idx=k%len(a)
    print(a[idx-1])