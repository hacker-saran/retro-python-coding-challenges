'''
Array K times rotation

I/P :
1
5 2
1 2 3 4 5

O/P:
4 5 1 2 3

'''

t = int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=n-(k%n) 
    x=l[m:n]+l[:m]
    print(*x,sep=' ')
