class Solution {
public:
    double average(vector<int>& salary) {
        double mini= 999999;
        double maxi = -1;
        for(int i =0;i<salary.size();i++){
            if(salary[i]>maxi){
                maxi= salary[i];
            }
            if(salary[i]<mini){
                mini = salary[i];
            }
        }
        double sum = 0;
        int n = 0;
        for(int j= 0;j<salary.size();j++){
            if(salary[j]!= maxi && salary[j] != mini){
                sum = sum + salary[j];
                n ++;

            }
        }
        return sum/n;
        
    }
};
