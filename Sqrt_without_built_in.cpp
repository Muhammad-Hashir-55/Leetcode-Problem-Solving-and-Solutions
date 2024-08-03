#include <iostream>
using namespace std;
class Solution{
public:
int mySqrt(int x){
    long long sqrt = 0;
    long long i=  0;
    while(i <= x){
        i = sqrt*sqrt;
        if(i >=x){
            break;
        }
        sqrt++;

    }
    if(i>x){
        return sqrt-1;
    }
    else{
        return sqrt;
    }
}
};
int main() 
{
    Solution check;
    cout<<check.mySqrt(8)<<endl;

}