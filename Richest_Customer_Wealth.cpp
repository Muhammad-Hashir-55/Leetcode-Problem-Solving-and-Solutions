class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        vector <int>vec;
        int sum = 0;
        for (int i = 0;i<accounts.size();i++){
            for(int j = 0;j<accounts[i].size();j++){
                sum = sum + accounts[i][j];

            }
            vec.push_back(sum);
            sum =0;
        }
        int maxi = -1;
        for(int k = 0;k<vec.size();k++){
            if(vec[k]>maxi){
                maxi = vec[k];
            }

        }
        return maxi;

        
    }
};
