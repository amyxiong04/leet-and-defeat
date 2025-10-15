class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # keeps track of the indices of days where we hvent found warmer temp
        res = [0] * len(temperatures)  # stores number of days until next warmer temp for each day
        for i, temp in enumerate(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res