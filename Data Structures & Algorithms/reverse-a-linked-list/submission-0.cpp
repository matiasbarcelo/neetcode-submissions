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

        vector<ListNode*> reverse_vect = vector<ListNode*>();
        ListNode* current_pointer = head;
        bool first_node = true;
        int count = -1;

        while(current_pointer != nullptr){
            count++;
            ListNode* current_node;
            if (! first_node){
                current_node = new ListNode(current_pointer->val, reverse_vect.at(count - 1));
            } else{
                current_node = new ListNode(head->val);
                first_node = false;
            }
            reverse_vect.push_back(current_node);
            current_pointer = current_pointer->next;
        }
        return reverse_vect.at(count);
    }
};
