'''
HOLLOW DIAMOND MATRIX PATTERN


Input  : 5

Output : 

* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 

'''

n=int(input())
x=1;r=2*n
for i in range(r):
    if i>=n:
        x-=1 
    for j in range(r):
        if j>=n-x+1 and j<n+x-1 :
            print(" ",end=' ')
        else:
            print("*",end=' ')
    if i<n:
        x+=1 
    print()
