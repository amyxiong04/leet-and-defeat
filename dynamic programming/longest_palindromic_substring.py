class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        # every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # check all substring lengths from 2 up to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 3 or dp[i + 1][j - 1]:
                        dp[i][j] = True

                        if length > max_len:
                            start = i
                            max_len = length

        return s[start:start + max_len]
    

    # but usually this approach is more intuitive (expand around center):
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > len(res):
                res = odd

            even = expand(i, i + 1)
            if len(even) > len(res):
                res = even

        return res