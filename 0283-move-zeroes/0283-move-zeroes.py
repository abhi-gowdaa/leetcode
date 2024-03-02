#brute
# class Solution(object):
#     def moveZeroes(self, nums):
#         n=len(nums)
#         temp=[]
#         k=0
#         for i in range(n):
#             if nums[i]!=0:
#                 temp.append(nums[i])
#                 k+=1
#         for i in range(k,n):
#             temp.append(0)
#         for i in range(n):
#             nums[i]=temp[i]
#optimal
class Solution(object):
    def moveZeroes(self,a):
        n=len(a)
        j = -1
        # Place the pointer j
        for i in range(n):
            if a[i] == 0:
                j = i
                break

        # No non-zero elements
        if j == -1:
            return a

        # Move the pointers i and j and swap accordingly
        for i in range(j + 1, n):
            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j += 1

        return a