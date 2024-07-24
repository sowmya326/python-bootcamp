#input as given asABC skip va;lue is 4 so
#after A 4 values if we skip them E same as for BC
#so output is EFG
str="ABC"
for i in str:
    print(chr(ord(i)+4),end="")