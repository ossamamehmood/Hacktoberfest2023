#include <iostream>
#include <regex>
#include <string>
using namespace std;
bool isValidIPAddress(const string &ipAddress) {
    // Regular expression pattern for a valid IPv4 address
    // 25[0-5]: Matches numbers from 250 to 255.
    // 2[0-4][0-9]: Matches numbers from 200 to 249.
    // [01]?[0-9][0-9]?: Matches numbers from 0 to 199. Here's the breakdown:
    // [01]?: Matches either 0 or 1, or nothing (since ? means 0 or 1 occurrence).
    // [0-9]: Matches any digit (0-9).
    // [0-9]?: Matches 0 to 9 (optional).
    regex pattern("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$");

    // Check if the ipAddress matches the pattern
    return regex_match(ipAddress, pattern);
}

int main() {
    string ipAddress;
    cout << "Enter an IP address: ";
    cin >> ipAddress;

    if (isValidIPAddress(ipAddress)) {
        cout << "Valid IP address: " << ipAddress << endl;
    } 
    else {
        cout << "Invalid IP address: " << ipAddress << endl;
    }
    return 0;
}
