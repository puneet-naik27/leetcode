def count_ways(n):
    # Base cases: If there are 0 or 1 players, only one way to pass the ball
    if n == 0 or n == 1:
        return 1

    # Initialize variables
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    # Calculate the number of ways iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Test the function
n = int(input("Enter the number of players in the queue: "))
ways = count_ways(n)
print("Number of ways to pass the ball:", ways)
