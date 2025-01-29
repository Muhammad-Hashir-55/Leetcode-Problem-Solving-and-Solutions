class Solution {
public:
    int countElements(vector<int>& nums) {
        int n = nums.size();
        int c= 0;
        for(int i = 0;i<n;i++){
            bool c1 = false;
            bool c2 = false;
            for(int j  =0;j<n;j++){
                if(nums[i]==nums[j]){
                    continue;
                }
                if(nums[i]>nums[j] and c1 ==false){
                    c1 = true;

                }
                if(nums[i]<nums[j] and c2 ==false){
                    c2 = true;
                }
                if(c1 == true and c2 == true){
                    c +=1;
                    break;
                }
            }

        }
        return c;
        
    }
};
