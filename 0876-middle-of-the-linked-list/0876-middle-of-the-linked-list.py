# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#tortise and rabbit(slow moves by 1 and fast moves by 2)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
        
       
            #brute solution in c++       
# Node *findMiddle(Node *head) {

# if(head->next==NULL){
#     return head;
# }
# Node* temp=head;
# Node* tempe=head;
# int count=1;

# while(temp->next!=NULL){
#     count++;
#     temp=temp->next;
# }

# count=(count/2)+1;
# int cnt=1;
# while(cnt!=count-1){
#     cnt++;
#     tempe=tempe->next;
#     }
# return tempe->next;
# }
