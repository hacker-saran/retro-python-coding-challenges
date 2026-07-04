'''
Toogle the case of World if all are same

Input  : Programming is EASY
Output : Programming IS easy

'''

s=input().split()
for i in s:
    lower,upper=0,0 
    for j in i:
        if j.islower():
            lower+=1 
        else:
            upper+=1 
    if lower==len(i):
        print(i.upper(),end=' ')
    elif upper==len(i):
        print(i.lower(),end=' ')
    else:
        print(i,end=' ')
