#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int maximum69Number (int num) {
        vector<int>vec1;
        if(num == 6 or num == 9){
            return 9;
        }
        long int new_num=0;
        int mod;
        while(num!=0){
            mod = num%10;
            vec1.push_back(mod);
            num = num /10;

        }
        vector<int>new_list;
        for (int i = vec1.size()-1;i>=0;i--){
            new_list.push_back(vec1[i]);
        }
        for (int j = 0;j<new_list.size();j++){
            if(new_list[j]==6){
                new_list[j] = 9;
                break;
            }
        
        }
        for (int k = 0;k<new_list.size();k++){
            new_num = new_num*10 + new_list[k];
        }
        return new_num;
        
    }
};
