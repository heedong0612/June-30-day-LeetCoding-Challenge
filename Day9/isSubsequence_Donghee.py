# Donghee Lee
# 06/09/2020

class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        
        for i in range(len(s)) :
            if t == "" : 
                return True
            
            if t[0] == s[i] :
                t = t[1:]
            
        return t == ""
        