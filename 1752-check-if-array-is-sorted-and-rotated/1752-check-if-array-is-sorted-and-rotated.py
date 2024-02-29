class Solution:
    
    
    def check(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)-1):
            
            if nums[i]> nums[i+1]:
                rotated_nums = nums[i + 1:] + nums[:i + 1]
                return rotated_nums == sorted(rotated_nums)
            
                  
        return True
            
    
    
# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         a=nums
#         nums.sort()
#         if a==nums:
#             return True
#         else:
#             return False
        