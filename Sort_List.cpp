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
ListNode * findmid(ListNode * head){
    ListNode * slow = head;
    ListNode * fast = head->next;
    while(fast->next != NULL && fast->next->next != NULL){
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
ListNode * merge(ListNode *left,ListNode * right){
    if(left ==NULL){
        return right;
    }
    if(right == NULL){
        return left;
    }
    if(left->val <= right->val){
        left->next = merge(left->next,right);
        return left;
    }
    else{
        right->next = merge(left,right->next);
        return right;

    }
}
ListNode * mergesort(ListNode *head){
    if(head == NULL || head->next == NULL){
        return head;

    }
    ListNode *left = head;
    ListNode * mid = findmid(head);
    ListNode * right = mid->next;
    mid->next = NULL;
    left = mergesort(left);
    right = mergesort(right);
    return merge(left,right);

}
    ListNode* sortList(ListNode* head) {
        head = mergesort(head);
        return head;
        
    }
};
