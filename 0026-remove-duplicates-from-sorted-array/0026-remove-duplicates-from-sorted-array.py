class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr=nums 
#for my reference ,unnecessary
        k=0
        for j in range(1,len(nums)):
            if arr[j]!=arr[k]:
                arr[k+1]=arr[j] #this replace dupli ele next to the unique ele [1,2,2,3]=>[1,2,3,2]
                k+=1
        return k+1 #returns index util the non duplicate ele
        