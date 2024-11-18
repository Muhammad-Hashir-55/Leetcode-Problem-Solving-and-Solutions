
 // Definition for singly-linked list.
 //struct ListNode {
 //     int val;
  //    ListNode *next;
  //    ListNode() : val(0), next(nullptr) {}
  //    ListNode(int x) : val(x), next(nullptr) {}
   //   ListNode(int x, ListNode *next) : val(x), next(next) {}
 // };
 
class Solution {
public:
    void add_node(ListNode * &head,ListNode * &tail,int x){
        ListNode * temp  =new ListNode();
        temp->val = x;
        temp->next = NULL;
        if(head == NULL){
            head = temp;
            tail = temp;
        }
        else{
            tail->next = temp;
            tail = temp;
        }
    }
    ListNode* oddEvenList(ListNode* head) {
        ListNode * tail = NULL;
        vector<int>vec;
        ListNode * temp = head;
        while(temp != NULL){
            vec.push_back(temp->val);
            temp = temp->next;

        }
        vector<int>ans;
        int n = vec.size();
        for(int i = 0;i<n;i+=2){
            ans.push_back(vec[i]);
        }
        for(int i = 1;i<n;i+=2){
            ans.push_back(vec[i]);
        }
        head = NULL;
        for(int i = 0;i<n;i++){
            add_node(head,tail,ans[i]);

        }
        return head;

        
    }
};
