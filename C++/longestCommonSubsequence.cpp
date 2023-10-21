#include <iostream>
#include <string>
using namespace std;

string longestCommonSubsequence(string str1, string str2, int m, int n) {
    if (m == 0 || n == 0)
        return "";

    if (str1[m-1] == str2[n-1])
        return longestCommonSubsequence(str1, str2, m-1, n-1) + str1[m-1];//append common character at last
    //if last character in m doesn't match
    string lcs1 = longestCommonSubsequence(str1, str2, m-1, n); 
     //if last character in n doesn't match
    string lcs2 = longestCommonSubsequence(str1, str2, m, n-1);

    if (lcs1.length() > lcs2.length())
        return lcs1;
    else
        return lcs2;
}

int main() {
    string str1 = "ABCDE";
    string str2 = "ACE";

    int m = str1.length();
    int n = str2.length();

    string lcs = longestCommonSubsequence(str1, str2, m, n);

    cout << "Longest Common Subsequence: " << lcs << endl;

    return 0;
}
