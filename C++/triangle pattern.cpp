#include <iostream>

int main() {
    int n;
    std::cout << "Enter the number of rows for the triangle: ";
    std::cin >> n;

    for (int i = 1; i <= n; i++) {
        // Print spaces
        for (int j = 1; j <= n - i; j++) {
            std::cout << " ";
        }

        // Print asterisks
        for (int k = 1; k <= 2 * i - 1; k++) {
            std::cout << "*";
        }

        // Move to the next line
        std::cout << std::endl;
    }

    return 0;
}
