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
    ListNode* insertionSortList(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode * sorted = NULL;
        while(head != NULL){
            ListNode * current = head;
            head= head->next;
            if(sorted == NULL || sorted->val >= current->val){
                current->next = sorted;
                sorted = current;
            }
            else{
                ListNode * temp = sorted;
                while(temp->next != NULL and temp->next->val < current->val){
                    temp = temp->next;
                }
                current->next = temp->next;
                temp->next= current;
            }
        }
        head = sorted;
        return head;
        
    }
};
