# Given a string, find the longest substring which is a palindrome.
def longest_palindromic_substring(s):
    n = len(s)
    # Create a table to store whether substrings are palindromes or not.
    dp = [[False] * n for _ in range(n)]
    
    start = 0  # Start index of the longest palindromic substring found so far.
    max_length = 1  # Length of the longest palindromic substring found so far.
    
    # All substrings of length 1 are palindromes.
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for palindromes of length 3 or more.
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

# Example usage:
input_string = "babad"
result = longest_palindromic_substring(input_string)
print("Longest Palindromic Substring:", result)
