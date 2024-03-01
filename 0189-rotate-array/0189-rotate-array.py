#brute
#class Solution:
#    def rotate(self, arr: List[int], k: int) -> None:
#         temp=[]
#         n=len(arr)
#         k=k%n+1 #if l=r +1 or else dont put +1 (k=k%n)
#         for i in range(k):
#             temp.insert(i,arr[i])
#         j=0   

#         for i in range(k,n):
#             arr[j]=arr[i]
#             j+=1

#         for i in range(k):
#             arr[n-k+i]=temp[i]

#         return arr

#optimal
class Solution:
    
    def rotate(self, arr: List[int], k: int) -> None:
        
        n=len(arr)
        k=k%n
        def swap(arr,start,end):
            while start<=end:
                temp=arr[start]
                arr[start]=arr[end]
                arr[end]=temp
                start+=1
                end-=1

        swap(arr, 0, n - 1)  # Reverse the entire array
        swap(arr, 0, k - 1)  # Reverse the first k elements
        swap(arr, k, n - 1)  # Reverse the remaining elements


        return arr
         