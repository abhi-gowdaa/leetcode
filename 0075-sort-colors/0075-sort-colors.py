class Solution(object):
    def sortColors(self, arr):
        n=len(arr)
        mid=0
        low=0
        high=n-1
        while mid<=high:

            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[high],arr[mid]=arr[mid],arr[high]
                high-=1


#better

# def sortArray(arr,n):
# 	cnt1=0
# 	cnt2=0
# 	cnt3=0
# 	for i in range(n):
# 		if arr[i]==0:
# 			cnt1+=1
# 		if arr[i]==1:
# 			cnt2+=1
# 		else:
# 			cnt3+=1
# 	for i in range(cnt1):
# 		arr[i]=0
# 	for i in range(cnt1,cnt2+cnt1):
# 		arr[i]=1
# 	for i in range(cnt2+cnt1,n):
# 		arr[i]=2
	
			



#brute
#sort algo
 



























			
	 
	
         
        