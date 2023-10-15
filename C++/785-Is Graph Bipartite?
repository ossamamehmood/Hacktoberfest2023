Intuition
Int these quostion we use concept of graph coloring using two colorss.If we are able to color the graph by only two colors than we can say that graph is bipartite.

Approach
This code implements a solution to the "Is Graph Bipartite?" problem. The problem asks whether it is possible to divide a given undirected graph into two sets such that every edge of the graph connects a vertex from one set to a vertex in the other set.
The implementation uses a modified breadth-first search (BFS) approach to traverse the graph and determine if it can be bipartite. It uses a queue q to store the vertices to be processed.
The main function isBipartite initializes a vector vis of the same size as the graph, representing the visited status of each vertex. The values in vis are initialized to 0, indicating that no vertices have been visited yet.
The function then iterates over each vertex in the graph. If a vertex has not been visited (vis[i] == 0), it is assigned to the first set by setting vis[i] to 1. The adjacent vertices of the current vertex i are added to the queue q, and their visited status is set to -1, indicating they belong to the second set.
The function then calls the fun function, passing the graph g, the visited vector vis, and the queue q. The fun function performs a modified BFS to check if the graph is bipartite.
In the fun function, while the queue q is not empty, it dequeues a vertex i. If the visited status of i is 1, it iterates over its adjacent vertices. If any adjacent vertex j is also assigned to the first set (vis[j] == 1), it means there is an edge within the same set, violating the bipartite property, so the function returns false. If j is not visited (vis[j] == 0), it assigns it to the second set by setting vis[j] to -1 and enqueues j.
If the visited status of i is -1, it performs a similar check but for vertices assigned to the second set. If any adjacent vertex j is assigned to the second set (vis[j] == -1), it returns false. If j is not visited (vis[j] == 0), it assigns it to the first set by setting vis[j] to 1 and enqueues j.
If the loop completes without any issues, it means the graph can be bipartite, and the function returns true.
Overall, the code checks if a given graph is bipartite by assigning vertices to two sets and performing a modified BFS to validate the bipartite property.

Complexity
Time complexity:O(V+E)O(V + E)O(V+E)
The time complexity of the code is O(V+E)O(V + E)O(V+E), where V is the number of vertices in the graph and E is the number of edges. This is because the code performs a modified BFS traversal of the graph, visiting each vertex and its adjacent vertices once. In the worst case, all vertices and edges of the graph will be visited.

Space complexity: O(V)O(V)O(V)
The space complexity of the code is O(V)O(V)O(V), where V is the number of vertices in the graph. This is because the code uses additional space to store the visited status of each vertex in the vis vector, which has a size equal to the number of vertices. Additionally, the code uses a queue to store the vertices to be processed during the BFS traversal. The maximum number of vertices that can be in the queue at any point is V. Therefore, the overall space complexity is O(V)O(V)O(V).


Code
class Solution {
public:
    bool fun(vector<vector<int>>&g, vector<int>&vis,queue<int>&q){
        while(!q.empty()){
            int i=q.front();
            q.pop();
            if(vis[i]==1){
                for(auto &j:g[i]){
                   if(vis[j]==1){
                       return false;
                   }
                    if(vis[j]==0){
                    vis[j]=-1;
                    q.push(j);
                    }
                }
            }
            else if(vis[i]==-1){
                for(auto &j:g[i]){
                   if(vis[j]==-1){
                       return false;
                   }
                    if(vis[j]==0){
                    vis[j]=1;
                    q.push(j);
                    }
                }
            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>>& g) {
        vector<int>vis(g.size(),0);
        queue<int>q;
        for(int i=0;i<g.size();i++){
            if(vis[i]==0){
                vis[i]=1;
                for(auto &j:g[i]){
                    q.push(j);
                    vis[j]=-1;
                }
                bool flag=fun(g,vis,q);
                if(!flag)return false;
            }
        }
        return true;
    }
};
