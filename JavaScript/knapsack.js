function knapsack(values, weights, capacity) {
    // Get the number of items
    const n = values.length;

    // Build a 2D array to store results for subproblems
    const dp = new Array(n + 1).fill(null).map(() => new Array(capacity + 1).fill(0));

    // Loop through each item
    for (let i = 1; i <= n; i++) {
        // Loop through each possible capacity
        for (let w = 1; w <= capacity; w++) {
            // Check if the weight of the current item can fit in the current capacity
            if (weights[i - 1] <= w) {
                // Calculate the maximum value when including and excluding the current item
                dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            } else {
                // If the current item's weight exceeds the capacity, we can't include it
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    //  Variables to track the selected items
    let totalValue = dp[n][capacity];  // Total value of selected items
    let totalWeight = capacity;        // Remaining capacity
    let selectedItems = [];           // List of selected item indices

    // Backtracking to find the selected items
    for (let i = n; i > 0 && totalValue > 0; i--) {
        if (totalValue !== dp[i - 1][totalWeight]) {
            // If the value changes, the current item is included
            selectedItems.push(i - 1);  // Adjust for 0-based indexing
            totalValue -= values[i - 1];
            totalWeight -= weights[i - 1];
        }
    }
    return {
        totalValue: dp[n][capacity],         // Total value of the selected items
        totalWeight: capacity - totalWeight, // Total weight used
        selectedItems: selectedItems.reverse() // List of selected item indices
    };
}

// Example usage:
let values = [10, 20, 30];
let weights = [1, 2, 3];
let capacity = 5;
let result = knapsack(values, weights, capacity);
console.log(result);
