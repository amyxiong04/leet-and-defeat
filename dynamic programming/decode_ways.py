class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1) # dp[i] = number of ways to decode the first i chars

        dp[0] = 1 # empty prefix
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])
    

    
# top down with memoization and recursion is more intuitive 
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            # Reached the end successfully:
            # this is 1 valid decoding
            if i == len(s):
                return 1

            # Strings starting with '0' are invalid
            if s[i] == '0':
                return 0

            # Already solved this subproblem
            if i in memo:
                return memo[i]

            # Option 1: take one digit
            ways = dfs(i + 1)

            # Option 2: take two digits if valid (10 to 26)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)