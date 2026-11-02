# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, profits, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main Program
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or len(weights) != n or len(profits) != n:
    print("Invalid input")

elif any(w <= 0 for w in weights) or any(p < 0 for p in profits):
    print("Invalid weights or profits")

elif capacity < 0:
    print("Invalid capacity")

else:
    result = knapsack(weights, profits, capacity)
    print("Maximum Profit:", result)

# Sample Input and Output
# Input=>
# Enter number of items: 3
# Enter weights: 10 20 30
# Enter profits: 60 100 120
# Enter knapsack capacity: 50


# Output=>
# Maximum Profit: 220