/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
// returns reverse from middle+1 node to compare
    ListNode* reverse(ListNode* head){
       ListNode* front=nullptr;
       ListNode* prev=nullptr;
     while(head!=nullptr)
     {
         front=head->next;
         head->next=prev;
         prev=head;
         head=front;  
     }
 return prev;
    }
    
//main function
      
    bool isPalindrome(ListNode* head)
{
    ListNode* slow=head; 
    ListNode* fast=head;
    
    while(fast->next!=nullptr && fast->next->next!=nullptr)
    {
        slow=slow->next;
        fast=fast->next->next;
    }
        
  ListNode* newNode=reverse(slow->next); // returns reverse of half llist
        
  ListNode* first=head;//0
  ListNode* second=newNode;//middle+1
 
        while(second!=NULL)
        {
            if(first->val!=second->val)
            {
            reverse(newNode);
            return false;
            }   
        first=first->next;
        second=second->next;    
       }
reverse(newNode);//bring back original ll
return true;
        
    }
};


// brute using stack
// #include<stack>
// bool isPalindrome(Node *head)
// {
// Node* temp=head;
// stack<int> st;

// while (temp!=NULL){
//     st.push(temp->data);
//     temp=temp->next;
// }
// temp=head;
// while(temp!=NULL){
//     if (st.top()==temp->data){
//         st.pop();
//         temp=temp->next;
//         continue;
//     }
//     return false;
// }
//     return true;

// }