#kadane's algorithm
class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        maxd = float('-inf') 
        sum=0
        for i in range(n):
            sum=sum+nums[i]
            maxd=max(maxd,sum)
            if sum<0:
                sum=0
            
        return maxd

 