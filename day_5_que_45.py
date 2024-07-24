#check how many vowels are there in a string

str=input()
cnt=0
v=['a','e','i','o','u']
for i in str:
    if i in v:
        cnt+=1
print(cnt)
#to convert lower to upper
check=['a','e','i','o','u']
count=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in check):
        cnt+=1
        print(count)
# write a program to consonants count
#we use len for space
#we can use list for input in str
vowel="aeiou"
consonent="bcdnghjklmnpqrstvwxyz"
count=0
c=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i not in vowel):
        count+=1
        print(count,consonent)