package main

import (
    "fmt"
)

func longestCommonSubsequence(text1 string, text2 string) int {
    m, n := len(text1), len(text2)
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }

    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if text1[i-1] == text2[j-1] {
                dp[i][j] = dp[i-1][j-1] + 1
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            }
        }
    }

    return dp[m][n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    text1 := "abcde"
    text2 := "ace"
    result := longestCommonSubsequence(text1, text2)
    fmt.Printf("Length of Longest Common Subsequence: %d\n", result)
}
