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
    ListNode* removeElements(ListNode* head, int val) {
        while(head != NULL && head->val == val){
            ListNode * deleting_node = head;
            head = head->next;
            delete deleting_node;
        }
        ListNode * temp = head;
        ListNode * previous = NULL;
        while(temp != NULL){
            if(temp->val == val){
                ListNode * deleting_node = temp;
                temp = temp->next;
                if(previous != NULL){
                    previous->next = temp;
                }
                delete deleting_node;
            }
            else{
                previous = temp;
                temp = temp->next;
            }

        }
        return head;
        
    }
};
