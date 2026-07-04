'''
FIBONACCI SERIES IN REVERSE ORDER

Input  : 5 
Output : 3 2 1 1 0

'''


n=int(input())
l=[0,1]
for i in range(2,n):
  l.append(l[i-1]+l[i-2])
print(l[::-1])
