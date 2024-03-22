/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <map>
//brute solution
// class Solution {
// public:
//     ListNode *detectCycle(ListNode *head) {
//     map<ListNode* , int> mpp; //we store node itself in the hash so i used Node*
    
//    ListNode* temp=head;
//   while(temp!=nullptr){
//       if(mpp.find(temp)!=mpp.end()){
//              return temp;
//          }
//         mpp[temp]=1;
//          temp=temp->next;
//      }
        
//      return NULL;
//     }
// };

//optimal using tortise and rabbit
class Solution {
public:
    ListNode *detectCycle(ListNode *head) 
{
   ListNode * fast=head;
   ListNode * slow=head;
   if (!head || !head->next){
       return nullptr;
   }
   while(fast->next!=NULL && fast->next->next!=NULL){
   slow=slow->next;
   fast=fast->next->next;
       if(slow==fast){
           slow=head;
           while(slow!=fast){
                   slow=slow->next;
               fast=fast->next;
               }
            return slow;
       }
   }
return nullptr;
}
    };
