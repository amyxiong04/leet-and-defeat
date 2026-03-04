class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        # To reach step i, you must have come from:

            # step i - 1 (by taking 1 step)

            # step i - 2 (by taking 2 steps)

        # soln = [0] * (n + 1)
        # soln[1] = 1
        # soln[2] = 2

        # for i in range(3, n + 1):
        #     soln[i] = soln[i - 1] + soln[i - 2]
        
        # return soln[n]

        # top down
        soln = [-1] * (n + 1)

        def dfs(i):
            if i <= 2:
                return i
            if soln[i] != -1:
                return soln[i]

            soln[i] = dfs(i - 1) + dfs(i - 2)
            return soln[i]

        return dfs(n)
