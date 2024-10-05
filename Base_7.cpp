class Solution {
public:
    string convertToBase7(int num) {
        if(num ==0){
            return "0";
        }
        bool c = false;
        if(num<0){
            num= abs(num);
            c = true;
        }
        string new_string = "";
        while(num){
            int mod = num %7;
            new_string = new_string + to_string(mod);
            num = num /7;

        }
        string ans ="";
        for(int i = new_string.size()-1;i>=0;i--){
            ans= ans + new_string[i];
        }
        if(c){
            return "-"+ans;
        }
        else{
            return ans;
        }
        
    }
};
