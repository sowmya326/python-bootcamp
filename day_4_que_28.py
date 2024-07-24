#****peack element****

my_list=list(map(int,input().split()))
cnt=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
        cnt+=i
        break
    print(my_list[cnt])

    #print all peak elements
