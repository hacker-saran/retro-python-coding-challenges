'''

Unique Number of Occurrences

Input: arr = [1,2,2,1,1,3]
Output: true
  
Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''
class Solution(object):
    def uniqueOccurrences(self, arr):
        d={}
        for i in arr:
            if i in d.keys():
               d[i]+=1 
            else:
                d[i]=1
        print(len(d),len(set(d.values())))
        if len(d)==len(set(d.values())):
            return True
        else:
            return False
