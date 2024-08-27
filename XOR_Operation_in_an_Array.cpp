class Solution {
public:
    int xorOperation(int n, int start) {
        vector<int>nums;
        int num = 0;
        for(int i = 0;i<n;i++){
            num = start + 2*i;
            nums.push_back(num);
        }
        int output = nums[0];
        for (int j = 1;j<nums.size();j++){
            output = output ^nums[j];
        }
        return output;
        
    }
};
