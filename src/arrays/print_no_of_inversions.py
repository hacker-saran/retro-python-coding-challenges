'''
Print No of inversions in a matrix i,e M[i][j]>M[p][q] & i<p & j<q

I/p:
2
3
1 2 3
4 5 6
7 8 9
2 
4 3
1 4

O/p:
0
2

'''

t=int(input())
for k in range(t):
    n=int(input())
    l=[] 
    for i in range(n):
        x=list(map(int,input().split()))
        l.append(x)
    c=0
    for i in range(n):
        for j in range(n):
            for a in range(i,n):
                for b in range(j,n):
                    if l[i][j]>l[a][b]:
                        c+=1 
    print(c)
                    
