# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         mapping = {
#             # num: index
#         }
#         for i, num in enumerate(nums):
#             diff = target - num
#             if diff in mapping:
#                 return [mapping[diff],i]
#             mapping[num]=i
#         return

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]+nums[j]==target):
#                     return [i,j]
         
    
 
class Solution:           
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in mapp:
                return [mapp[diff],i]
            mapp[num]=i
        return
         