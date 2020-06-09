import re
def isSubsequence(s: str, t: str) -> bool:
    '''
    Two solutions:
    1. Regex
        - Runtime ~9000ms lol
    2. Stack
        - Runtime ~40ms
    '''
    # Regex Solution
    
    # arr = re.split(r'', s)
    # p = r'\w*'
    # for ch in s:
    #     p += ch + '\w*'
    # pattern = re.compile(p)

    # match = pattern.match(t)
    # return match

    # Stack solution

    # edge case
    if s == '':
        return True

    # prepare stack
    stack = re.split(r'', s)
    stack.pop()
    stack.pop(0)
    stack = stack[::-1]

    for _, ch in enumerate(t):
        if ch == stack[-1]:
            stack.pop()
        if not stack: # if stack is empty
            return True
    
    return False