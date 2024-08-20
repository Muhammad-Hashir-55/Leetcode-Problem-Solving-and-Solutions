#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    char repeatedCharacter(string s) {
        vector<char>seen;
        int i =0;
        bool checking =false;
        for (i = 0;i<s.size();i++){
            for (int j = 0; j<seen.size();j++){
                if(seen[j] == s[i]){
                    checking = true;
                    return s[i];
                }
            }
            if(checking == false){
                seen.push_back(s[i]);
            }
        }
        return s[i];
    }
};