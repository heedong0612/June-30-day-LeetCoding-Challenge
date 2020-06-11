// 1 PASS
class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int curr = 0, ptr = nums.size() - 1, ptr2 = nums.size() - 1; 
        // ptr2 is an index for next 2 to come fill
        
        while (curr <= ptr) {
            
            if (nums[ptr] == 2) { // fill 2 in the back part
                nums[ptr] = nums[ptr2];
                nums[ptr2] = 2;
                ptr2--; // move the index to next available spot for 2
                ptr--;  
                
            } else if (nums[ptr] == 0) { // push it to the front part
                nums[ptr] = nums[curr];
                nums[curr] = 0;
                curr++;
                
            } else {
                ptr--;
            }
        }
        
    } 
};

// 2 PASSES

// class Solution {
// public:
//     void sortColors(vector<int>& nums) {
//         int r = 0, w = 0, b = 0;
        
//         for (int n: nums) {
//             if (n == 0) r++;
//             if (n == 1) w++;
//             if (n == 2) b++;
//         }
        
//         for (int i = 0; i < r; i++) {
//             nums[i] = 0;
//         }
        
//         for (int i = r; i < r + w; i++) {
//             nums[i] = 1;
//         }
        
//         for (int i = w + r; i < r+ w + b; i++) {
//             nums[i] = 2;
//         }
        
//     } 
// };
