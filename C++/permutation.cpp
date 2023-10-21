#include <iostream>
#include <string>
using namespace std;

void generatePermutations(string str, int left, int right) {
    if (left == right) {
        cout << str << endl;
    } else {
        for (int i = left; i <= right; i++) {
            swap(str[left], str[i]);                        //for combination
            generatePermutations(str, left + 1, right);     
            swap(str[left], str[i]);                        //for backtracking
        }
    }
}

int main() {
    string inputString;
    cout << "Enter a string: ";   //for n elements there will be n! permutations
    cin >> inputString;
    int n = inputString.length();
    cout << "All permutations in lexicographical order:\n";
    generatePermutations(inputString, 0, n - 1);
    return 0;
}

// #include <iostream>
// #include <algorithm>

// void printAllPermutations(std::string str) {
//     std::sort(str.begin(), str.end()); 
//     // Sort the string in lexicographical order initially
//     do {
//         std::cout << str << std::endl;
//     } while (std::next_permutation(str.begin(), str.end()));
//     // Generate next permutation until no more are possible
// }

// int main() {
//     std::string inputString;
//     std::cout << "Enter a string: ";
//     std::cin >> inputString;

//     std::cout << "All permutations in lexicographical order:\n";
//     printAllPermutations(inputString);

//     return 0;
// }

