class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        # Empty string has 1 valid decoding
        dp[n] = 1

        # Process from the end of the string back to the front
        for i in range(n - 1, -1, -1):
            # '0' cannot be decoded alone
            if s[i] == '0':
                dp[i] = 0
            else:
                # Use one digit
                dp[i] = dp[i + 1]

                # Use two digits if they form a number from 10 to 26
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    dp[i] += dp[i + 2]

        return dp[0]
    

    
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