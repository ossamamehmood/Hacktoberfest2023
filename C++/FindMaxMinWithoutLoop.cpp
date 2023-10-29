#include <iostream>
#include <vector>

// Using Recurssion 


int findMax(const std::vector<int>& numbers, int currentIndex, int currentMax) {
    if (currentIndex == numbers.size()) {
        return currentMax;
    }
    return findMax(numbers, currentIndex + 1, std::max(currentMax, numbers[currentIndex]));
}

int findMin(const std::vector<int>& numbers, int currentIndex, int currentMin) {
    if (currentIndex == numbers.size()) {
        return currentMin;
    }
    return findMin(numbers, currentIndex + 1, std::min(currentMin, numbers[currentIndex]));
}

int main() {
    std::vector<int> numbers = {3, 7, 1, 9, 2, 5, 8}; // this is for example you can create your own testcases

    int max = findMax(numbers, 0, numbers[0]);
    int min = findMin(numbers, 0, numbers[0]);

    std::cout << "Maximum: " << max << std::endl;
    std::cout << "Minimum: " << min << std::endl;

    return 0;
}
