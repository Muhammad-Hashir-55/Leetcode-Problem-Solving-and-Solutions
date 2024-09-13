class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int sum = 0;
        nums.push_back(0);
        vector<int>vec;
        for(int i =0;i<nums.size();i++){
            if(nums[i] == 1){
                sum++;
            }
            else{
                vec.push_back(sum);
                sum =0;
            }
        }
        int maxi= 0;
        for(int i =0;i<vec.size();i++){
            if(maxi<vec[i]){
                maxi = vec[i];
            }

        }
        return maxi;
        
    }
};
