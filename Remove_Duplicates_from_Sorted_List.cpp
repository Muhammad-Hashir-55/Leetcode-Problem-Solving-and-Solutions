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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode * temp = head;
        if(head == NULL || head->next == NULL){
            return head;
        }
        while(temp != NULL){
            ListNode * checking_node = temp->next;
            while(checking_node != NULL){
                if(checking_node->val == temp->val){
                    ListNode * next_node = checking_node->next;
                    temp->next = next_node;
                    delete checking_node;
                    checking_node = next_node;
                }
                else{
                    checking_node = checking_node->next;
                }
            }
            temp = temp->next;
        }
        return head;
    }
};
