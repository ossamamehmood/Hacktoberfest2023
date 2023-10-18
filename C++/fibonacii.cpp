#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    
    int n1 = -1, n2 = 1;
    for (int i = 0; i < n; ++i)
    {
        int n3 = n1 + n2;
        cout << n3 << ' ';
        n1 = n2;
        n2 = n3;
    }
    cout << endl;

    return 0;
}
