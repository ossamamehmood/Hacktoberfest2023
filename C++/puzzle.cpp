#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>

using namespace std;

struct PuzzleState {
    vector<vector<int>> board;
    int moves;
    int heuristic;
    int totalCost;

    bool operator>(const PuzzleState& other) const {
        return totalCost > other.totalCost;
    }
};

int calculateHeuristic(const vector<vector<int>>& board, const vector<vector<int>>& goal) {
    int h = 0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] != 0) {
                int row = (board[i][j] - 1) / 3;
                int col = (board[i][j] - 1) % 3;
                h += abs(row - i) + abs(col - j);
            }
        }
    }
    return h;
}

bool isGoalState(const vector<vector<int>>& board, const vector<vector<int>>& goal) {
    return board == goal;
}

vector<vector<int>> getNeighbors(const vector<vector<int>>& board) {
    vector<vector<int>> neighbors;
    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};
    int x, y;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == 0) {
                x = i;
                y = j;
                break;
            }
        }
    }
    for (int i = 0; i < 4; ++i) {
        int newX = x + dx[i];
        int newY = y + dy[i];
        if (newX >= 0 && newX < 3 && newY >= 0 && newY < 3) {
            vector<vector<int>> neighborBoard = board;
            swap(neighborBoard[x][y], neighborBoard[newX][newY]);
            neighbors.push_back(neighborBoard);
        }
    }
    return neighbors;
}

void solveEightPuzzle(const vector<vector<int>>& initial, const vector<vector<int>>& goal) {
    priority_queue<PuzzleState, vector<PuzzleState>, greater<PuzzleState>> pq;
    unordered_set<vector<vector<int>>> visited;
    
    PuzzleState initialState = {initial, 0, calculateHeuristic(initial, goal), calculateHeuristic(initial, goal)};
    pq.push(initialState);

    while (!pq.empty()) {
        PuzzleState current = pq.top();
        pq.pop();

        if (isGoalState(current.board, goal)) {
            cout << "Solution found in " << current.moves << " moves." << endl;
            return;
        }

        visited.insert(current.board);
        vector<vector<int>> neighbors = getNeighbors(current.board);
        for (const auto& neighbor : neighbors) {
            if (visited.find(neighbor) == visited.end()) {
                PuzzleState nextState = {neighbor, current.moves + 1, calculateHeuristic(neighbor, goal), 0};
                nextState.totalCost = nextState.moves + nextState.heuristic;
                pq.push(nextState);
            }
        }
    }

    cout << "No solution found." << endl;
}

int main() {
    vector<vector<int>> initial = {{1, 2, 3}, {5, 6, 0}, {7, 8, 4}};
    vector<vector<int>> goal = {{1, 2, 3}, {5, 8, 6}, {0, 7, 4}};

    solveEightPuzzle(initial, goal);

    return 0;
}
