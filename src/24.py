import sys
from collections import deque

def find_longest_palindromic_subsequence(s: str) -> int:
    if not s or len(s) == 1:
        return len(s)

    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row and column with 1s
    for i in range(n):
        dp[i][i] = 1

    max_length = 1

    # Fill the table
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if s[start] == s[end]:
                dp[start][end] = dp[start+1][end-1] + 1
                max_length = max(max_length, dp[start][end])
            else:
                dp[start][end] = max(dp[start+1][end], dp[start][end-1])

    return max_length

# Test the function
s = "aab"
print("Length of longest palindromic subsequence:", find_longest_palindromic_subsequence(s))
