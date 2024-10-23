#tc O(nlogn) bec use or sorting
#class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         mapp={}
#         length=0
#         maxlength=0
#         # nums.sort()
#         nums=set(nums)
#         print(nums)
#         for num in nums:
#             if  (num-1) in mapp:
#                 if num in mapp:
#                     pass
#                 else:
#                     mapp[num]=1
#                     length+=1
#             else:
#                 mapp[num]=1
#                 length=1
#             maxlength=max(maxlength,length)
#         return maxlength

#tc O(n) optimal
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length=0
        maxlength=0
        nums=set(nums)
        for num in nums:
            if (num-1) not in nums:
                length=0
                while (num+length) in nums:
                    length+=1
                maxlength=max(maxlength,length)
        return maxlength
