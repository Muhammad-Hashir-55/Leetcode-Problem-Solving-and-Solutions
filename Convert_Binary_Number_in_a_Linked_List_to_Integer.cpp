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
    int getDecimalValue(ListNode* head) {
        ListNode * temp = head;
        string new_string  ="";
        while(temp != NULL){
            new_string = new_string + to_string(temp->val);
            temp = temp->next;
        }
        int i = new_string.size();
        int ii = new_string.size()-1;
        int answer = 0;
        int power = 0;
        while(i>0){
            if(new_string[ii] =='1'){
                answer = answer + pow(2,power);
            }
            power++;
            ii--;
            i--;
       
        }
        return answer;
    }
};
