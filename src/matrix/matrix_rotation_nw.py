
''' 
Matrix Rotation

You are given a square matrix A of dimensions NxN. You need to apply the below given 3 operations on the matrix A.

-> Rotation: It is represented as R S where S is an integer in {90, 180, 270, 360, 450, ...} which denotes the number of degrees to rotate. You need to rotate the matrix A by angle S in the clockwise direction. The angle of rotation(S) will always be in multiples of 90 degrees.
-> Update: It is represented as U X Y Z. In initial matrix A (as given in input), you need to update the element at row index X and column index Y with value Z.
After the update, all the previous rotation operations have to be applied to the updated initial matrix.
-> Querying: It is represented as Q KL. You need to print the value at row index K and column index L of the matrix A.

Input :
The first line contains a single integer N.
Next N lines contain N space-separated integers Aij (i - index of the row, j - index of the column).
Next lines contain various operations on the array. Each operation on each line (Beginning either with R, U or Q). -1 will represent the end of input.

Output:
For each Query operation print the element present at row index K and colum index L of the matrix in its current state.

Explanation :
Sample Input :
2
1 2
3 4
R 90
Q 0 0
Q 0 1
R 90
Q 0 0
U 0 0 6
Q 1 1
-1

Initial matrix 
1 2 
3 4 

For R 90, clockwise rotation by 90 degrees, the matrix will become
3 1
4 2
For Q 0 0, print the element at row index 0 and column index O of A, which is 3. For Q 0 1, print the element at row index O and column index 1 of A, which is 1.
Again for R 90, clockwise rotation by 90 degrees, the matrix will become
4 3
2 1
For Q 0 0, print the element at row index 0 and column index O of A, which is 4.
For U 0 0 6, update the value at row index O and column index O in the initial matrix to 6. So the updated matrix will be,
6 2
3 4
After updating, we need to rotate the matrix by sum of all rotation angles applied till now(i.e. R 90 and R 90 90 + 90⇒ 180 degrees in clockwise direction).
After rotation the matrix will now become
4 3
2 6
Next for Q 11, print the element at row index 1 and column index 1 of A, which is 6.
So the output should be 
Sample Output :
3
1 
4
6

'''



# Code

n=int(input())
in_matrix=[]
for i in range(n):
    in_matrix.append(list(map(int,input().split())))
 
def rotation(matrix):
    k=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            k[i][j] = matrix[n-j-1][i]
    return k

rotCount = 0
matrix = in_matrix
while True:
    usin = input().strip()
    if usin=='-1':
        break
    usin = usin.split()
    if usin[0]=='R':
        angle = (int(usin[1])//90)%4
        rotCount += angle 
        while angle:
            matrix = rotation(matrix)
            angle-=1
    elif usin[0]=='Q':
        row, col = map(int,usin[1:])
        print(matrix[row][col])
    elif usin[0]=='U':
        row, col, val = map(int,usin[1:])
        matrix = in_matrix
        matrix[row][col] = val 
        while rotCount:
            matrix = rotation(matrix)
            rotCount-=1 
    
