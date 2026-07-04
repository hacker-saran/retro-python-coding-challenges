'''
Two String Equal-Undo

The program must accept two strings s1,s2. The character # represent undo action to clear the last entered character.
The program must print YES if two strings are equal else print NO as output.

Input:
kee#y 
rs##kee#y

Input:
abcdefghi###jklmnop##qrst##dfbjhere#######
###abc###abcdefjklmn####klmnqrd 

Output:
YES

''' 



def hello(s):
    x='';c=0
    for i in range(len(s)-1,-1,-1):
        if s[i]!='#' and c==0:
            x+=s[i] 
        if s[i]=='#':
            c+=1  
        
        elif c>0:
            c-=1 
    return x[::-1]
a=list(input().strip())
b=list(input().strip()) 
if hello(a)==hello(b):
    print("YES")
else:
    print("NO")


        
        
        
