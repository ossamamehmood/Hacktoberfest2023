#include<iostream>
#include<string>
using namespace std;
int main()
{
    string na;
    string n;
    int i, j, l;
    cout << "Enter Main String: ";
    getline(cin, na);
    cout << "Enter Sub String: ";
    cin >> n;
    l = n.length();
    bool found = false; 
    for (i = 0; i <= na.length() - l; i++) { 
        //Avoid overflow limit -> (na+n)
        for (j = 0; j < l; j++) {
            if (na[i + j] != n[j]) {
                break;
            }
        }
        if (j == l) {
            cout << i + 1 << " Is the String index number" << endl;
            found = true; 
        }
    }
    if (!found) { 
        cout << "Sub String Not found" << endl;
    }
    return 0;
}
