# class Solution:
#     def containsDuplicate(self,nums:List[int])->bool:
#         maps={}
#         for num in nums:
#             if num in maps:
#                 return True
#             else:
#                 maps[num]=1
#         return False




1
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # ll=set()
#         # for i in range(len(nums)):
#         #     if nums[i] in ll:
#         #         return True
#         #     else:
#         #         ll.add(nums[i])
#         # return False

# 2
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         #return len(nums)!=len(set(nums))



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st=set()
        for num in nums:
            if num in st:
                return True
            else:
                st.add(num)
        return False

      