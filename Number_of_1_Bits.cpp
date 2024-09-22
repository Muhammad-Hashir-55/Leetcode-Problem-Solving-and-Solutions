class Solution {
public:
    int hammingWeight(int n) {
        int binary[32];
        int i = 0;
        while(n >0){
            binary[i] = n %2;
            n = n/2;
            i++;
        }
        int ones =0;
        for(int j =0;j<i;j++){
            if(binary[j]==1){
                ones++;
            }
        }
     return ones;   
    }
};
