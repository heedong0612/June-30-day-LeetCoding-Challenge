// Donghee Lee
// 06/11/2020

/** Linear Search**/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        for (int i = 0; i < nums.size(); i++) 
            if (nums[i] >= target) return i;
        
        return nums.size();
    }
};

/**** Binary Search *****

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int i = 0, j = nums.size(), mid;
        
        while (i < j) {
            mid = i + (j - i) / 2;
            if (target == nums[mid]) return mid;   
            
            if (target < nums[mid]) {
                j = mid;
            } else {
                i = mid + 1;
            }
        }
        
        return i;
    }
};

*/