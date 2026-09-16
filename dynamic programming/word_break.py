class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] = whether first i chars can be segmented

        dp[0] = True # empty prefix is successfully segmented

        if s[0] in wordDict:
            dp[1] = True

        for i in range(2, n + 1):
            for j in range(i):  # j is the split point
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[n]
        