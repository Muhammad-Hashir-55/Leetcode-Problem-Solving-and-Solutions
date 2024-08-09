#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int checking  = false;
        for (int i = 0;i < n;i++){
            checking = false;
            for (int j = 0;j<n;j++){
                if (i == nums[j]){
                    checking = true;
                }
                
            }
            if (checking == false){
                return i;
            }

        }
        return n;

        
    }
};
