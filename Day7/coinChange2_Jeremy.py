from typing import List

def change(amount: int, coins: List[int]) -> int:
    '''
    not my implementation
    submitted for the sake of streak
    '''
    dp = [0 for _ in range(amount + 1)]

    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]