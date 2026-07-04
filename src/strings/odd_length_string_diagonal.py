'''

Odd Length String Diagonal

Input : cry 
Output:
c y
 r
c y

'''

s=input().strip()
ind=0
for i in range(len(s)):
    for j in range(len(s)):
        if i==j:
            print(s[ind],end='')
        elif j==len(s)-i-1:
            print(s[len(s)-ind-1],end='')
        else:
            print(" ",end='')
    print()
    ind+=1            
