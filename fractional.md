def fractional_knapsack(capacity, items):
    # items is a list of tuples: (profit, weight)
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    total_profit = 0
    
    for profit, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_profit += profit
        else:
            total_profit += profit * (capacity / weight)
            break
            
    return total_profit

# Example usage:
items = [(60, 10), (100, 20), (120, 30)] # (profit, weight)
print("Maximum Profit:", fractional_knapsack(50, items))
