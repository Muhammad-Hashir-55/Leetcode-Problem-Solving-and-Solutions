class Solution {
public:
    int balancedStringSplit(string s) {
        int no_of_substrings = 0;
        int balance = 0;
        for (int i =0;i < s.size();i++){
            if(s[i]=='L'){
                balance++;
            }
            else{
                balance--;
            }
            if(balance ==0){
                no_of_substrings++;
            }
        }
        return no_of_substrings;
        
    }
};
