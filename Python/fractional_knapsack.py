def fractional_knapsack(items, capacity):
    # Sort items by their value-to-weight ratio in descending order (greedy step)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        item_weight, item_value = item

        if capacity >= item_weight:
            # Take the whole item if it fits in the knapsack
            knapsack.append((item_weight, item_value))
            total_value += item_value
            capacity -= item_weight
        else:
            # Take a fraction of the item to fill the knapsack to capacity
            fraction = capacity / item_weight
            knapsack.append((capacity, item_value * fraction))
            total_value += item_value * fraction
            break  

    return total_value, knapsack

if __name__ == "__main__":
    items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
    knapsack_capacity = 15

    max_value, selected_items = fractional_knapsack(items, knapsack_capacity)

    print("Maximum value:", max_value)
    print("Selected items:")
    for weight, value in selected_items:
        print(f"Weight: {weight}, Value: {value}")
