class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for v in nums:
            if  v in hashset:
                return True
            hashset.add(v)
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         num = set()
#         count=0
#         for v in range(len(nums)):
#             if nums[v] in num:
#                 return True
#             num.add(nums[v])
               
         
