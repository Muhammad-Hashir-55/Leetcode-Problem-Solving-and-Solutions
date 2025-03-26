#include <vector>
#include <algorithm>

class Solution {
public:
    bool canSortArray(std::vector<int>& nums) {
        std::vector<int> k = nums;
        std::sort(k.begin(), k.end());
        int n = nums.size();
        
        while (true) {
            bool c = false;
            for (int i = 0; i < n - 1; ++i) {
                bool c1 = false;
                for (int j = i + 1; j < n; ++j) {
                    if (nums[i + 1] < nums[i]) {
                        int x1 = __builtin_popcount(nums[i]);
                        int x2 = __builtin_popcount(nums[i + 1]);
                        if (x1 == x2) {
                            std::swap(nums[i], nums[i + 1]);
                            c = true;
                            c1 = true;
                            break;
                        }
                    }
                }
                if (c1) {
                    break;
                }
            }
            if (!c) {
                break;
            }
        }
        
        return nums == k;
    }
};
