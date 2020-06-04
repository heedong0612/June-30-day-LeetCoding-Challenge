class Solution:
    def reverseString(s) -> None:
        size = len(s)
        middle = size // 2
        for i, letter in enumerate(s[0:middle]):
            print(i)
            temp = s[i]
            s[i] = s[-i - 1]
            s[-i - 1] = temp