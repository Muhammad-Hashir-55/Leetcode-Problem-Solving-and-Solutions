#include <iostream>
using namespace std;
class Solution {
public:
    string truncateSentence(string s, int k) {
   
    
    
        string ss [s.size()];
        int index =0;
        int i =0;
        string new_string = "";
        while(index<s.size()){
            if(s[index]!=' '){
                new_string = new_string + s[index];
            }
            else{
                ss[i] = new_string;
                new_string ="";
                i++;
            }
            index++;
            
        }
        if(i == k-1){
            return s;
        }
        string stri;
        for(int j =0;j<k;j++){
            if(j ==0){
                stri = stri + ss[j];
            }
            else{
                stri = stri+ " " + ss[j];
            }

        }
        return stri;
        
    }
};
