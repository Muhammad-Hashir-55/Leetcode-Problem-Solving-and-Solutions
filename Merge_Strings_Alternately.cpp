class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string new_string;
        if(word1.size() == word2.size()){
            for (int i = 0;i<word1.size();i++){
                new_string = new_string + word1[i];
                new_string = new_string + word2[i];
            }
            return new_string;
        }
        else if (word1.size()>word2.size()){
            int i = 0;
            for (i = 0;i<word2.size();i++){
                new_string = new_string + word1[i];
                new_string = new_string + word2[i];
            }
            for(int j = i;j<word1.size();j++){
                new_string =new_string + word1[j];
            }
            return new_string;
        }
        else{
                 int i = 0;
            for (i = 0;i<word1.size();i++){
                new_string = new_string + word1[i];
                new_string = new_string + word2[i];
            }
            for(int j = i;j<word2.size();j++){
                new_string =new_string + word2[j];
            }
            return new_string;

        }
        return new_string;
        
    }
};
