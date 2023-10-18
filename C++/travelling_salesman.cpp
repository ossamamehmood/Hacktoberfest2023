#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int tsp(int mask, int pos, const vector<vector<int>>& graph, vector<vector<int>>& memo) {
    int n = graph.size();
    if (mask == (1 << n) - 1) {
        return graph[pos][0];
    }

    if (memo[mask][pos] != -1) {
        return memo[mask][pos];
    }

    int minCost = INF;
    for (int city = 0; city < n; ++city) {
        if ((mask & (1 << city)) == 0) {
            int newMask = mask | (1 << city);
            int cost = graph[pos][city] + tsp(newMask, city, graph, memo);
            minCost = min(minCost, cost);
        }
    }

    memo[mask][pos] = minCost;
    return minCost;
}

int main() {
    int n = 4; // Number of cities
    vector<vector<int>> graph = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    vector<vector<int>> memo(1 << n, vector<int>(n, -1));
    int minCost = tsp(1, 0, graph, memo); // Start from city 0 (mask = 1)

    cout << "Minimum cost of the TSP tour: " << minCost << endl;

    return 0;
}
