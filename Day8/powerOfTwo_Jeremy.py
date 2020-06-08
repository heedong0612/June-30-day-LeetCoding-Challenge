def isPowerOfTwo(n: int) -> bool:
    '''
    O(n)
    There should be a bitwise solution 
    '''
    if n == 1:
        return True
    if n <= 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n //= 2
    
    return True

if __name__ == "__main__":
    n = 16
    print(isPowerOfTwo(n))