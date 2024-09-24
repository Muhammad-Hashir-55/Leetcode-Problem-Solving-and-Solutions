class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int att =0;
        vector<int>vec;
        vec.push_back(att);
        for(int i =0;i<gain.size();i++){
            att = att + gain[i];
            vec.push_back(att);
        }
        int maxi = vec[0];
        for(int i =0;i<vec.size();i++){
            if(vec[i]>maxi){
                maxi = vec[i];
            }
        }
        return maxi;
    }
};
