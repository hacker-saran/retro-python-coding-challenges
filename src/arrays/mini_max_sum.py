'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input  :
1 2 3 4 5 

Output : 
10 14
'''


import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    print(sum(arr)-max(arr),sum(arr)-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
