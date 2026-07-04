'''
The program must accept a number matrix having R rows and C columns. Then the program must check whether a number is repeated consecutively for 3 times either in a row, in a column or along a diagonal. If there are more than one such repeated numbers then the program must print the minimum value V. The program must print -1 if no such value is repeated.
Note: C = R+1
Boundary Condition(s):
1 <= R <= 20
Input Format:
The first line contains R.
The next R lines contain C integer values separated by a space.
Output Format:
The first line contains V.
Example Input/Output 1:
Input:
7
2 3 4 5 6 2 4 3
2 3 4 7 6 7 6 2
2 3 5 5 5 5 2 5
2 3 1 1 2 1 3 6
10 1 1 1 9 0 3 51
2 10 1 1 5 1 51 7
5 2 10 1 1 51 2 1
Output:
1
Explanation:
The repeated values are 5 1 2 3 10 51.
The minimum value is 1.
'''

n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
nums=[]
for i in range(n):
    for j in range(len(l[0])-2):
        if l[i][j]==l[i][j+1] and l[i][j+1]==l[i][j+2]:
            if l[i][j] not in nums:nums.append(l[i][j])

for j in range(n+1):
    for i in range(n-2):
        if l[i][j]==l[i+1][j] and l[i+1][j]==l[i+2][j]:
            if l[i][j] not in nums:nums.append(l[i][j])


for i in range(n):
    for j in range(len(l[0])):
       
        x,y = i,j
        c=0
        while(x<n-1 and y<len(l[0])-1):
            if l[x][y]==l[x+1][y+1] :
                c+=1
            else:
                c=0
            if c==2 and l[x][y] not in nums:
                nums.append(l[x][y])
            x+=1
            y+=1
        x,y = i,j
       
        while(x<n-1 and y>0):
            if l[x][y]==l[x+1][y-1]:
                c+=1
            else:
                c=0
            if c==2 and l[x][y] not in nums:
                nums.append(l[x][y])
            x+=1
            y-=1
if len(nums)==0:
    print("-1")
else:
    print(min(nums))

