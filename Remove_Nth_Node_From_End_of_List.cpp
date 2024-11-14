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
    int sizz(ListNode *head){
        int n = 0;
        while(head != NULL){
            n ++;
            head = head->next;
        }
        return n;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int ind = sizz(head) - n;
        if(ind ==0){
            head = head->next;
            return head;
        }
        else if(ind == sizz(head)-1){
            ListNode * temp = head;
            ListNode * prev = NULL;

            while(temp->next != NULL){
                prev = temp;
                temp = temp->next;
            }
            prev->next= NULL;
            temp = NULL;
            return head;

        }
        else{
            ListNode * temp = head;
            int ii= 0;
            ListNode * prev = NULL;
            while(temp != NULL){
                if(ii == ind){
                    ListNode * dele = temp;
                    prev->next = temp->next;
                    delete dele;
                    return head;

                }
                prev = temp;
                temp = temp->next;
                ii ++;
            }
        }
        return head;
        
    }
};
