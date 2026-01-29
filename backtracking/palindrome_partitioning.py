class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i) -> None:
            if i == len(s):
                res.append(path.copy())
                return

            for end in range(i, len(s)):
                if is_palindrome(i, end):
                    path.append(s[i:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res

