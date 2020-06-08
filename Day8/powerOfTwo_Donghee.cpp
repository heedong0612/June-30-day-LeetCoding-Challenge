class Solution {
public:
    /*
    
    1 =  1
    2 =  10
    4 =  100
    8 =  1000
    16 = 10000
    32 = 100000
    64 = 1000000
    128= 10000000
    ...
    
     */
    
    bool isPowerOfTwo(int n) {
        
        while (n > 1) {
            if (n & 1 == 1)     // if last digit is not zero
                return false;    
            n >>= 1;  
        }
        return n == 1;
    }
    
};