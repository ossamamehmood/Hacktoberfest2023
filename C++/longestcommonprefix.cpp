#include <bits/stdc++.h>
using namespace std;

string longestCommonPrefix(string arr[], int n)
{
	// take temp_prefix string and assign first element of
	// arr : a.
	string result = arr[0];
	int len = result.length();

	// Iterate for rest of element in string.
	for (int i = 1; i < n; i++) {
		// .find() return index of that substring from
		// string.
		while (arr[i].find(result) != 0) {

			// update matched substring prefx
			result = result.substr(0, len - 1);
			len--;

			// check for empty case. direct return if true..
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
