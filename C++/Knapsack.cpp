#include <iostream>
#include <vector>

using namespace std;

// Structure to represent an item with weight and value
struct Item {
    int weight;
    int value;
};

// Function to solve the 0/1 Knapsack Problem using dynamic programming
int knapsackDP(const vector<Item>& items, int capacity) {
    int n = items.size();
    // Create a DP table to store the maximum value for different item counts and capacities
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    for (int i = 1; i <= n; ++i) {
        for (int w = 0; w <= capacity; ++w) {
            // If the current item's weight can fit in the knapsack
            if (items[i - 1].weight <= w) {
                // Choose the maximum value between two options:
                // 1. Not including the current item
                // 2. Including the current item and adding its value
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value);
            } else {
                // If the item's weight exceeds the current capacity, skip it
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // The final value in the DP table represents the maximum value achievable
    return dp[n][capacity];
}

int main() {
    int capacity;
    cout << "Enter the knapsack capacity: ";
    cin >> capacity;

    // Define a list of items with their weights and values
    vector<Item> items = {
        {2, 12},
        {1, 10},
        {3, 20},
        {2, 15}
    };

    // Call the knapsackDP function to find the maximum value
    int maxValue = knapsackDP(items, capacity);

    // Display the result
    cout << "The maximum value that can be obtained is: " << maxValue << endl;

    return 0;
}
