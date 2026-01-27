class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def dfs(start: int, total: int):
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                dfs(i + 1, total + candidates[i])  # i+1 because each element used once
                curr.pop()

        dfs(0, 0)
        return res