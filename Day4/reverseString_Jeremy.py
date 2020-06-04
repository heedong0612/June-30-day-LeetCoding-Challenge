from typing import List

def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     temp = s[i]
        #     back = -(i + 1)
        #     s[i] = s[back]
        #     s[back] = temp
        
        s.reverse()