#include <bits/stdc++.h>
using namespace std;

string longestCommonPrefix(string arr[], int n)
{
	
	string result = arr[0];
	int len = result.length();

	
	for (int i = 1; i < n; i++) {
		while (arr[i].find(result) != 0) {

			result = result.substr(0, len - 1);
			len--;

			if (result.empty()) {
				return "-1";
			}
		}
	}
	return result;
}

/* Driver Function to test other function */
int main()
{
	string input[]
		= { "geeksforgeeks", "geeks", "geek", "geezer" };
	int n = sizeof(input) / sizeof(input[0]);
	cout << "The longest Common Prefix is : "
		<< longestCommonPrefix(input, n);
	return 0;
}
