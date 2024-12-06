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
    void reorderList(ListNode* &head) {
        ListNode * temp = head;
        vector<int> arr;
        while(temp != NULL){
            arr.push_back(temp->val);
            temp = temp->next;
        }
        vector<int>ans;
        int i =0;
        int j = arr.size()-1;
        int n = j+1;
        while(i<=j){
            ans.push_back(arr[i]);
            ans.push_back(arr[j]);
            i++;
            j--;
        }
        if(n %2 != 0){
            ans.pop_back();
        }
        ListNode *head1 = NULL;
        ListNode * tail = NULL;
        for(int i= 0;i<n;i++){
            ListNode * temp = new ListNode(ans[i]);
            if(head1 == NULL){
                head1 = temp;
                tail = temp;
            }
            else{
                tail->next = temp;
                tail = temp;
            }
        
            
        }
        temp = head1->next;
        ListNode * mainn = head;
        while(temp != NULL){
            mainn->next= temp;
            temp = temp->next;
            mainn = mainn->next;

        }
        return;
    }
};
