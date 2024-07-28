#include <iostream>
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        if (n <=1){
            return 1;
        }
        int size = n + 1;
        int arr[size];
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 2;
        for (int i = 3; i <size;i++){
            arr[i] = arr[i-1] + arr[i-2];
        }
        return arr[n];
        
    }
};
int main() 
{
    Solution check;
    cout<<check.climbStairs(10)<<endl;
    
    
return 0;
}