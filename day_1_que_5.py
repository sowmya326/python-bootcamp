#mr Z is selected for olympics he is participating in swimming competition only one winner is selected among all the participants and mr X and mrY are friends of Z
#me X is participating in badminton mr y is participating mr y is participating in table tennis according to the selection commitee the requriement for badminton players are
#height 140cm weight factors of 2 body fat is less than 12% for badminton
#according to the selection commitee requirements for table tennis are height menimum 118 to 148cm weight no of medals won by mr Z body fat 14%
#according to the pervious history Z participated in 14 games out of which he is having success rate of 65%
#write a program to check wheather mr x,y,z travel in a same plane or not

mr_x="badminton"
mr_y="tabletennis"
mr_z="swimming"
selected=mr_z
heightx=int(input("enter height of x:"))
weightx=int(input("enter weight of x:"))
fact7=(50*14)/100
heighty=int(input("enter height of y:"))
heighty=int(input("enter weight of y:"))
if(heightx>=140 and weightx%2==0):
    if(heighty>=118 or heighty<=148 and  weighty%fact7==0):
        print("all went in same plane")
    else:
        print("only x,z went in same plane")
else:print("only z went in plane")

