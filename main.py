def min_coins(coins, target_amount):
    # ""code here""
    # Initialize a DP array with a value larger than the possible minimum coins
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed for an amount of 0

    # Fill the DP table
    for amount in range(1, target_amount + 1):
        for coin in coins:
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the target amount is unreachable, return -1
    return dp[target_amount] if dp[target_amount] != float('inf') else -1

""" # testing
coins = [1, 4, 6, 9, 14]
target_amount = 26
result = min_coins(coins, target_amount)
print(result)  # Output: 3 """
