#include <iostream>
#include <stack>
using namespace std;

int main() {
    // create a stack of strings
    stack<string> languages;
    
    // add element to the Stack
    languages.push("C++");
    languages.push("Java");
    languages.push("Python");
    
    // print top element
    cout << languages.top();

    return 0;
}
