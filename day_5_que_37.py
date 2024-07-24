# if the input is given as XYZ then it should be print ABC because after XYZ there is no cyclic format ABC we should print************imp
#XYZ
#X=120+3=123
#chr(123)
#Y=121+3=124
#chr(124)=}
#Z=122+3=125
#chr(125)=~             #home work

str="XYZ"
for i in str:
    print(chr((ord(i)+3)-26),end="")