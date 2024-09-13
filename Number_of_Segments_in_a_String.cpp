class Solution {
public:
    int countSegments(string s) {
        s = s + " ";
        vector<string>vec;
        string new_string= "";
        for(int i =0;i<s.size();i++){
            if(s[i]!= ' '){
                new_string = new_string + s[i];
                
            }
            else{
                if(new_string != ""){
                    vec.push_back(new_string);
                new_string = "";

                }
            
            }
        }
        return vec.size();
    }

};
