# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #brute using stack
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp=head
#         st=[]
#         while temp!=None:
#             st.append(temp.val)
#             temp=temp.next
  
#         temp=head
#         while temp!=None:
#             temp.val=st.pop()
#             temp=temp.next;
#         return head;
 
    
 #optimal   
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        front=None
        prev=None
        while(temp!=None):
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev