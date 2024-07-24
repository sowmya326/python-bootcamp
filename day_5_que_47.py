#print all the values follwed by the consonents

vowels=['a','e','i','o','u']
consonent="bcdnghjklmnpqrstvwxyz"
ans=""
i="hello wOrld"
inp=i.lower()
for i in inp:
     if(i in vowels):
        ans+=i
for i in inp:
    if(i in consonent):
        ans+=i
        

