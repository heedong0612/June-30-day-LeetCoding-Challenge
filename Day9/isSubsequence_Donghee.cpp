// Donghee Lee
// 6/9/2020

class Solution {
public:
    bool isSubsequence(string t, string s) {
        
        for (int i = 0; i < s.length(); i++) {
            if (t[0] == s[i]) 
                t = t.substr(1);      

            if (t == "") return true;
        }     
        return t == "";
    }
};