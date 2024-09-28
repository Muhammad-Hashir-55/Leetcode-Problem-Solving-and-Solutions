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
    ListNode* middleNode(ListNode* head) {
        ListNode * temp = head;
        vector<int>vec;
        while(temp !=NULL){
            vec.push_back(temp->val);
            temp = temp->next;
        }
        int index = 0;
        if(vec.size()%2 ==0){
            index = vec.size()/2;
        }
        else{
            index = (vec.size()-1)/2;
        }
        temp = head;
        int i =0;
        while(temp != NULL){
            if(i == index){
                head = temp;
                break;
            }
            i++;
            temp = temp->next;
        }
        return head;
    }
};
