class Solution {
public:
    void reverseString(vector<char>& s) {
        char temp;
        
        // iterate through half
        for (int i = 0; i < s.size() / 2; i++) {
            temp = s[s.size() - 1 - i];
            s[s.size() - 1 - i] = s[i];
            s[i] = temp;
        }
        
    }
};