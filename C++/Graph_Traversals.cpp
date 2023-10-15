/*
Problem Statement:
Implement different graph traversal methods (DFS, BFS) in C++.
Provide user with the choice to select the traversal method.

Traversals to Implement:
1. Depth First Search (DFS)
2. Breadth First Search (BFS)

Graph Representation:
For simplicity, we'll use an adjacency list representation of an undirected graph.

Traversing Methods:
1. Depth First Search (DFS): Visit nodes as deep as possible before moving to the next branch.
2. Breadth First Search (BFS): Visit all the neighbors of a node before moving to the next level.

Complexities:
1. Depth First Search (DFS): 
   Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
   Space Complexity: O(V) for recursive stack.

2. Breadth First Search (BFS):
   Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges.
   Space Complexity: O(V) for queue.

*/

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

class Graph {
    int V; 
    vector<vector<int>> adjList;
    
public:
    Graph(int V) : V(V), adjList(V) {}

    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    void DFS(int start) {
        vector<bool> visited(V, false);
        stack<int> stack;
        stack.push(start);
        visited[start] = true;

        while (!stack.empty()) {
            int node = stack.top();
            stack.pop();
            cout << node << " ";

            for (int neighbor : adjList[node]) {
                if (!visited[neighbor]) {
                    stack.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
    }

    void BFS(int start) {
        vector<bool> visited(V, false);
        queue<int> queue;
        queue.push(start);
        visited[start] = true;

        while (!queue.empty()) {
            int node = queue.front();
            queue.pop();
            cout << node << " ";

            for (int neighbor : adjList[node]) {
                if (!visited[neighbor]) {
                    queue.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
    }
};

int main() {
    Graph g(6);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 4);
    g.addEdge(3, 5);
    g.addEdge(4, 5);

    int choice;
    cout << "Choose Traversal Method:" << endl;
    cout << "1. Depth First Search (DFS)" << endl;
    cout << "2. Breadth First Search (BFS)" << endl;
    cin >> choice;

    cout << "Traversal Starting from Node 0:" << endl;
    if (choice == 1) {
        g.DFS(0);
    } else if (choice == 2) {
        g.BFS(0);
    } else {
        cout << "Invalid Choice!" << endl;
    }

    return 0;
}
