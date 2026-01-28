class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr, open_cnt, close_cnt):
            if open_cnt == n and close_cnt == n:
                res.append("".join(curr))
                return

            if open_cnt < n:
                curr.append("(")
                dfs(curr, open_cnt + 1, close_cnt)
                curr.pop()

            if close_cnt < open_cnt:
                curr.append(")")
                dfs(curr, open_cnt, close_cnt + 1)
                curr.pop()

        dfs([], 0, 0)
        return res
            
