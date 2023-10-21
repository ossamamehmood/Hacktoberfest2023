#include<iostream>
#include<map>
using namespace std;

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);

    map<char, int> charCount;

    for(char c : str) {
        if(isalpha(c)) {  // Only consider alphabetic characters
            charCount[c]++;
        }
    }

    cout << "Character frequencies:\n";
    for(auto& pair : charCount) {
        cout << pair.first << ": " << pair.second << " times\n";
    }
    return 0;
}
