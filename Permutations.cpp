class Solution {
public:
vector<vector<int>> ans;
void swap(vector<int>&nums,int i,int j){
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;

}
    void permu(vector<int> nums,int start,int end){
        if(start == end){
            ans.push_back(nums);
        }

        for(int i= start;i<=end;i++){
            swap(nums,start,i);
            permu(nums,start+1,end);
            swap(nums,start,i);



        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        permu(nums,0,n-1);
        return ans;

        
    }
};
