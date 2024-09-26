class Solution {
public:
    int pivotInteger(int n) {
        int x = n;
        if(n ==1){
            return 1;
        }
        while(x!=0){
            x--;
            if(x<=0){
                return -1;
            }
            int sum1 =0;
            for(int i =1;i<x+1;i++){
                sum1 = sum1 + i;
            }
            int sum2 = 0;
            for(int j =x;j<n+1;j++){
                sum2 = sum2 + j;
            }
            if(sum1 == sum2){
                return x;
            }
        }
        return x;
        
    }
};
