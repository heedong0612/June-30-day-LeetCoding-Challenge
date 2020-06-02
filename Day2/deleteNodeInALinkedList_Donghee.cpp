/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // faster : copies one element and deletes the duplicate
    void deleteNode(ListNode* node) {       
        node->val = node->next->val;
        node->next = node->next->next;
    }
    
    
// slower : copies all elements after the node down by one
//     void deleteNode(ListNode* node) {      
    
//         while (node->next->next != nullptr) {
//             node->val = node->next->val;
//             node = node->next;
//         }
//         node->val = node->next->val;
//         node->next = nullptr;
//     }
};