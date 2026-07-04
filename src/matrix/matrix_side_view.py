'''
Matrix side view 
If given character is "l" or "L" print the first alphabet in each row from left to right.
If given character is "r" or "R" print the first alphabet in each row from right to left.

I/p:
4 6 
e - y - r k
- x i - - - 
- - - a t q 
- m - - p a 
L

O/p:
exam

'''

r,c = map(int,input().split())
l=[] 
for i in range(r):
    s=''
    x=list(map(str,input().split()))
    for i in x:
        if i.isalpha():
            s+=i
    l.append(s)
ch=input().strip()
if ch=='l' or ch=='L':
    for i in l: print(i[0],end='')
elif ch=='r' or ch=='R':
    for i in l:print(i[-1],end='')
print(l)
