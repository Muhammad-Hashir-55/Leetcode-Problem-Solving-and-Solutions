class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        vector<string>vec;
        for(int i = 0;i<paths.size();i++){
            for (int j = 0;j<paths[i].size();j++){
                vec.push_back(paths[i][j]);
                
            }
        }
        int count = 0;
        int k = 1;
        for ( k = 1;k<vec.size();k=k+2){
            count = 0;
            for (int l = 0;l<vec.size();l++){
                if(vec[k]==vec[l]){
                    count++;
                }
            }
            if(count ==1){
                return vec[k];
            }

        }
        return vec[k];
        
    }
};
