/*
    [1 2 5]
    
    0 1 2 3 4 5 6 7 8 9 10 
    ---------------------------------
    1 1 2 2 3 4 5 6 7 8 10  
    1 1 1 1 1 1 1 1 1 1 1  
    ---------------------------------
    1                             = 1
    1+1, 2                        = 2
    1+1+1, 1+2                    = 2
    1+1+1+1, 1+1+2, 2+2           = 3
    1+1+1+1+1, 1+1+1+2, 1+2+2, 5  = 4

*/

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1);
        dp[0] = 1;
        
        for (int c : coins) {
            for (int i = c; i < dp.size(); i++) {
                dp[i] += dp[i - c];
            }
        }
        
        return dp[amount];
    }
};
