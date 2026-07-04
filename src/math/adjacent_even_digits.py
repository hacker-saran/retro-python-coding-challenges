'''

ADJACENT EVEN DIGITS 

Print the digits surrounded by the even digits. If not any one, print -1.

Input  : 1268916787
Output : 1678

'''



n=input().strip()
p=0
if int(n[1])%2==0:
    print(n[0],end='')
    p=1
for i in range(1,len(n)-1):
    if int(n[i-1])%2==0 and int(n[i+1])%2==0 :
        print(n[i],end='')
        p=1
if int(n[-2])%2==0 :
    print(n[-1])
    p=1 
if p==0:
    print("-1")

