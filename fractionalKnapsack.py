# Fractional Knapsack using Greedy Method
def fractional_knapsack(weights, profits, capacity):

    n = len(weights)
    
    # Calculate profit/weight ratio
    ratio = []

    for i in range(n):
        ratio.append(profits[i] / weights[i])

    # Sort items by ratio in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if ratio[i] < ratio[j]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                weights[i], weights[j] = weights[j], weights[i]
                profits[i], profits[j] = profits[j], profits[i]

    total_profit = 0

    # Select items according to capacity
    for i in range(n):

        if weights[i] <= capacity:
            total_profit += profits[i]
            capacity -= weights[i]

        else:
            total_profit += profits[i] * (capacity / weights[i])
            break

    return total_profit

# Main Program
n = int(input("Enter number of items: "))

weights = list(map(float, input("Enter weights: ").split()))
profits = list(map(float, input("Enter profits: ").split()))
capacity = float(input("Enter knapsack capacity: "))

if n <= 0 or len(weights) != n or len(profits) != n:
    print("Invalid input")

elif any(w <= 0 for w in weights) or any(p < 0 for p in profits):
    print("Weights must be positive and profits non-negative")

elif capacity < 0:
    print("Capacity cannot be negative")

else:
    result = fractional_knapsack(weights, profits, capacity)
    print("Maximum Profit:", round(result, 2))



# OUTPUT:=
#Enter number of items: 3
#Enter weights: 10 20 30
#Enter profits: 60 100 120
#Enter knapsack capacity: 50