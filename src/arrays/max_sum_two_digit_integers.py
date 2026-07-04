'''The program must accept an integer N as the input. The program must print the maximum possible sum S obtained by adding the two digit integers formed from the digits of N as the output. If the number of digits is odd, then one digit must be excluded from the sum as it is not possible to form two digit integer.
Boundary Condition(s):
10 <= N <= 10^9
Input Format:
The first line contains the value of N.
Output Format:
The first line contains the value of S.
Example Input/Output 1:
Input:
1452
Output:
93
Explanation:
Here the formed two digit integers are 51 and 42. So their sum is 93.
''' 

n=input().strip()
n=list(map(int,n))
n.sort()
i=0
if(len(n)%2==1):
    i=1
j=len(n)-1
s=0

while(i<j) :
    k=int(str(n[j])+str(n[i]))
    s+=k
    i+=1
    j-=1 
print(s)
