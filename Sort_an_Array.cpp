class Solution {
public:
    void merge(vector<int>&nums,int l,int mid,int r){
        int n1 = mid -l+1;
        int n2 = r-mid;
        int a[n1];
        int b[n2];
        for(int i = 0;i<n1;i++){
            a[i] = nums[i+l];
        }
        for(int i =0;i<n2;i++){
            b[i] = nums[mid+1+i];
        }
        int i=  0;
        int j = 0;
        int k = l;
        while(i<n1 && j<n2){
            if(a[i]<=b[j]){
                nums[k] = a[i];
                i++;
                k++;
            }
            else{
                nums[k] = b[j];
                j++;
                k++;

            }
        }
        while(i<n1){
            nums[k] = a[i];
            i++;
            k++;
        }
        while(j<n2){
            nums[k] = b[j];
            j++;
            k++;
        }


    }
    void mergesort(vector<int>&nums,int l,int r){
        
        if(l<r){
            int mid = (l + r)/2;
            mergesort(nums,l,mid);
            mergesort(nums,mid+1,r);
            merge(nums,l,mid,r);
        }
    
    }
    vector<int> sortArray(vector<int>& nums) {
        int left = 0;
        int right = nums.size()-1;
        
        mergesort(nums,left,right);
        return nums;
        
        
    }
};
