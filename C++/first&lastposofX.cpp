#include <bits/stdc++.h>
pair<int, int> findFirstLastPosition(vector<int> &arr, int n, int x)
{
    pair<int, int> ans;
    if (arr.size() == 0)
        return {-1, -1};
    int left = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
    int right = upper_bound(arr.begin(), arr.end(), x) - arr.begin();
    if (left >= n)
    {
        return {-1, -1};
    }
    if (arr[left] == x)
    {
        return {left, right - 1};
    }
    return {-1, -1};
}

using namespace std;
int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; i++)
        cin >> arr[i];

    int X;
    cin >> X;

    pair<int, int> sol = findFirstLastPosition(arr, N, X);
    cout << sol.first << " " << sol.second << endl;
}
