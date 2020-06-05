class Solution {
public:
    
    /* 
    bruteforce: 
    
    1) make a list of weight amount of elements 
    2) pick a random number of that length (of sum of weights)
    3) return what is at that index
    
    that's a lot of space + time to add that many elements.. sooo
    
    more ideal:
    1) pick a random number of that length (of sum of weights)
    2) have a vector of ranges
    
    */
    
    int wSum;
    int wSize;
    vector<int> ran; // range
        
    Solution(vector<int>& w) {
       wSum = 0; 
        wSize = w.size();
    
        for (int i = 0; i < w.size(); i++) {
            wSum += w[i];
            ran.push_back(wSum);
        }
        
    }
    
    int pickIndex() {
        int r = rand() % wSum;
        
        /* binray search: optimized to O(log n) */
        int start = 0, end = wSize, mid; // end is exclusive
        while (start < end) {
            mid = start + (end - start) / 2;
            
            if (r >= ran[mid]) { // >= because the weight could've been 0 and that should not count
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        
        return end;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */