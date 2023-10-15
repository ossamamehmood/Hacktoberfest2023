#include <iostream>

using namespace std;

int factorial(int n) {
  if (n == 0 || n == 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

int main() {
  int n;
  cout << "Enter a number: ";
  cin >> n;

  int factorial = factorial(n);
  cout << "The factorial of " << n << " is " << factorial << endl;

  return 0;
}
