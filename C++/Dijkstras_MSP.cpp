#include <iostream>
#include <vector>
// #include <queue>
#include <climits>

using namespace std;

#define INF INT_MAX

// Structure to represent an edge in the graph


// Function to find the vertex with the minimum distance value
int minDistance(const vector<int>& distance, const vector<bool>& visited, int V) {
    int minDist = INF;
    int minIndex = -1;

    for (int i = 0; i < V; i++) {
        if (!visited[i] && distance[i] < minDist) {
            minDist = distance[i];
            minIndex = i;
        }
    }

    return minIndex;
}

// Function to print the minimal spanning tree
void printMST(const vector<int>& parent, const vector<vector<int>>& graph, int V) {
    cout << "Edge \tWeight\n";
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " - " << i << "\t" << graph[i][parent[i]] << "\n";
    }
}

// Function to implement Dijkstra's Minimal Spanning Tree Algorithm using Greedy search
void dijkstraMST(const vector<vector<int>>& graph, int V, int source) {
    vector<int> distance(V, INF); // Array to store the minimum distance from the source
    vector<bool> visited(V, false); // Array to track visited vertices
    vector<int> parent(V, -1); // Array to store the parent of each vertex in the MST

    distance[source] = 0; // Distance of the source vertex is set to 0

    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(distance, visited, V); // Find the vertex with the minimum distance value
        visited[u] = true; // Mark the vertex as visited

        for (int v = 0; v < V; v++) {
            // Update the distance of the neighboring vertices of the current vertex if it's smaller
            if (!visited[v] && graph[u][v] && distance[u] != INF && distance[u] + graph[u][v] < distance[v]) {
                distance[v] = distance[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }

    printMST(parent, graph, V); // Print the minimal spanning tree
}

int main() {
    int V; // Number of vertices
    cout << "Enter the number of vertices: ";
    cin >> V;

    vector<vector<int>> graph(V, vector<int>(V, 0)); // Adjacency matrix to represent the graph
    //graph(V, vector<int>(V, 0)): This initializes the 2D vector "graph" with V rows and V columns. Each element of the vector is initialized to 0 using the vector<int>(V, 0) syntax.
    cout << "Enter the weighted adjacency matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {   
            cin >> graph[i][j];
        }
    }

    int source; // Source vertex
    cout << "Enter the source vertex: ";
    cin >> source;

    dijkstraMST(graph, V, source); // Find the minimal spanning tree using Dijkstra's algorithm

    return 0;
}

//    0   1  2  3  4  5  6  7  8
// 0[ 0, 4, 0, 0, 0, 0, 0, 8, 0 ],
// 1[ 4, 0, 8, 0, 0, 0, 0, 11, 0 ],
// 2[ 0, 8, 0, 7, 0, 4, 0, 0, 2 ],
// 3[ 0, 0, 7, 0, 9, 14, 0, 0, 0 ],
// 4[ 0, 0, 0, 9, 0, 10, 0, 0, 0 ],
// 5[ 0, 0, 4, 14, 10, 0, 2, 0, 0 ],
// 6[ 0, 0, 0, 0, 0, 2, 0, 1, 6 ],
// 7[ 8, 11, 0, 0, 0, 0, 1, 0, 7 ],
// 8[ 0, 0, 2, 0, 0, 0, 6, 7, 0 ]
