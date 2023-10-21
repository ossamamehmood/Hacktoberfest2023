#include <iostream>
#include <string>
using namespace std;
string lexicographicalMaxString(string s) {
    string maxString = s;
    int n = s.length();
    s += s;//circular form

    for (int i = 1; i < n; i++) {
        string current = s.substr(i, n);
        if (current > maxString) {
            maxString = current;
        }
    }

    return maxString;
}

int main() {
    string inputString;
    cout << "Enter a string: ";
    cin >> inputString;

    string result = lexicographicalMaxString(inputString);
    cout << "Lexicographically maximum string: " << result << endl;

    return 0;
}
