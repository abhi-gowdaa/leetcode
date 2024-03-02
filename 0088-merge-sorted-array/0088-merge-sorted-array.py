# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         k=0
#         ans=[]
#         for i in range(m):
#             nums1.append(nums2[k])
#             nums1.remove(0)
#             k+=1
#         j=0
#         for i in range(len(nums1)):
#             if nums1[i]!=0:
#                 ans.append(nums1[i])
#                 j+=1
                
#         nums1.sort()
       
#         return ans
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
