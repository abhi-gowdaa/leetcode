# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#         #[-4,-2,-2,-1,1]
#         closest_num = nums[0] #-4 
#         closest_distance = abs(closest_num) # 4
        
#         for num in nums:
#             distance = abs(num) #4 , 2 ,1 ,1
#             if distance < closest_distance: #4 < 4 ,2<4 , 1 < 2 ,1<1
#                 closest_num = num            #-2 , -1
#                 closest_distance = distance    #2 ,1
#             elif distance == closest_distance and num > closest_num: #4==4 and -4>-4  , 1 ==1 and 1>-1
#                 closest_num = num  #1

#         return closest_num
    
    

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest=nums[0]
        for i,num in enumerate(nums):
            if abs(num) < abs(closest):
                closest=num
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
             return closest
            
        