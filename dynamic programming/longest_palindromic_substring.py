class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j] = whether s[i:j+1] is a palindrome

        max_start = 0
        max_len = 1
        
        # length 1: all chars by themselves are palindromes
        for i in range(n):
            dp[i][i] = True

        # length 2
        for i in range(n - 1):
            if s[i + 1] == s[i]:
                dp[i][i + 1] = True

                max_len = 2
                max_start = i

        # length 3 and above
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if (j - i + 1) > max_len:
                            max_len = j - i + 1
                            max_start = i

        return s[max_start: max_start + max_len]