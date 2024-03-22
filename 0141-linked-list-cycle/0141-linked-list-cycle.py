# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #optimal
    def hasCycle(self, head: Optional[ListNode]) -> bool:   
        if not head or not head.next:
            return False
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False

        
                #list brute
# def detectCycle(head):
#     has=[]
#     temp=head
#     while temp!=None:
#         if temp in has:
#             return True 
#         has.append(temp)
#         temp=temp.next
#     return False

                  # #set
# def detectCycle(head):
#     has=set()
#     temp=head
#     while temp!=None:
#         if temp in has:
#             return True 
#         has.add(temp)
#         temp=temp.next
#     return False
    
          
        