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