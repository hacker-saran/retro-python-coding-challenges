'''
Trapping Rain Water

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''

class Solution:
    def trap(self, height: List[int]) -> int:

        w=0
        n=len(height)
        lm = height[0]
        for i in range(1,n-1):
            rm=max(height[i+1:])
            m=min(lm,rm)
            if lm<height[i]:lm=height[i]
            if(height[i]>m):continue
            w+=m-height[i] 
        return w
