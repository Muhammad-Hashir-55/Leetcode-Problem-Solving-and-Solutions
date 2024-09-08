class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        bool checking = false;
        int countarr =0;
        int counttar = 0;
        for(int k =0;k<arr.size();k++){
            countarr =0;
            counttar =0;
            for(int l=0;l<arr.size();l++){
                if(arr[k]==arr[l]){
                    countarr++;
                }

            }
            for(int m=0;m<target.size();m++){
                if(arr[k]==target[m]){
                    counttar++;
                }
            }
            if(countarr !=counttar){
                return false;
            }

        }
        for(int i =0;i<arr.size();i++){
            checking = false;
            for(int j =0;j<target.size();j++){
                if(arr[i]==target[j]){
                    checking = true;
                }

            }
            if(checking == false){
                return false;
            }

        }
        return true;
    }
};
