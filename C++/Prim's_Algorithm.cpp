// Prim's Algorithm in CPP

#include <bits/stdc++.h>
using namespace std;

// Number of vertices in the graph
#define V 6

int minKey(int key[], bool mst[])
{
	// Initialize min value
	int min = INT_MAX, min_index;

	for (int v = 0; v < V; v++)
		if (mst[v] == false && key[v] < min)
			min = key[v], min_index = v;

	return min_index;
}


void print(int parent[], int G[V][V])
{
	cout << "Edge \tWeight\n";
	for (int i = 1; i < V; i++)
		cout << parent[i] << " - " << i << " \t"
			<< G[i][parent[i]] << " \n";
}

void prim(int G[V][V])
{
	int parent[V];
    int key[V];
    bool mst[V];

	for (int i = 0; i < V; i++)
    {
		key[i] = INT_MAX, mst[i] = false;
    }  

	key[0] = 0;

	// First node is always root of MST
	parent[0] = -1;

	// The MST will have V vertices
	for (int count = 0; count < V - 1; count++) {
		int u = minKey(key, mst);
        mst[u] = true;
        for (int v = 0; v < V; v++)
        {
              if (G[u][v] && mst[v] == false
				&& G[u][v] < key[v])
				parent[v] = u, key[v] = G[u][v];
        }
	}

	// Print the constructed MST
	print(parent, G);
}


int main()
{
	int G[V][V] = { { 0, 4, 6, 0, 0, 0},
						{ 4, 0, 6, 3, 4, 0 },
						{ 6, 6, 0, 1, 8, 0 },
						{ 0, 3, 1, 0, 2, 3 },
						{ 0, 4, 8, 2, 0, 7},
            { 6, 0, 0, 3, 7, 0} };

	prim(G);
    return 0;
}

