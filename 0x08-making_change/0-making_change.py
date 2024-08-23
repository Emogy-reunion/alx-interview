def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create an array to store the minimum coins needed for each value up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make 0

    # Iterate through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] if using the coin results in fewer coins
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, then it's not possible to make the total
    return dp[total] if dp[total] != float('inf') else -1
