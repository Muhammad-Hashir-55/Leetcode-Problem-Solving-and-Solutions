class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        vector<int>vec;
        int i = 1;
        bool checking  = false;
        while(vec.size()<k){
            checking = false;
            for (int j = 0;j<arr.size();j++){
                if(i == arr[j]){
                    checking  = true;
                }
            }
            if(checking == false){
                vec.push_back(i);

            }
            i++;
        }
        return vec[k-1];
    }
};
