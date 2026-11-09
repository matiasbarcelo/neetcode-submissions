using namespace std;
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
        ListNode* reverseList(ListNode* head) {
            if (head == nullptr){
                return nullptr;
            }
            if (head->next == nullptr){
                return head;
            }
            
            // we have to save the current pointer as the prior pointer    
            ListNode* prior_pointer = head;
            // the current pointer is now the prior pointer's next field
            ListNode* current_pointer = head->next;
            // before making current pointer next null, since it contains the next node, save it
            ListNode* next_pointer = current_pointer->next;;            
            // and the current_pointer's next field now points to that prior node
            current_pointer->next = prior_pointer;
            // since it's the first node, the prior pointer's next is now nullptr
            prior_pointer->next = nullptr;
            // make the prior_pointer the current_pointer and the current pointer the next pointer
            prior_pointer = current_pointer;
            current_pointer = next_pointer;
    
            while(current_pointer != nullptr){
                next_pointer = current_pointer->next;
                current_pointer->next = prior_pointer;
            
                prior_pointer = current_pointer;
                current_pointer = next_pointer;
            }

            return prior_pointer;
        }
};
