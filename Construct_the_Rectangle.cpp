#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> constructRectangle(int area) {
        vector<int>vec;
        int starting = sqrt(area);
        for (int i = starting;i>0;i--){
            if(area % i == 0){
                vec.push_back(area/i);
                vec.push_back(i);
                return vec;
            }
        }
        return vec;
        }
};
