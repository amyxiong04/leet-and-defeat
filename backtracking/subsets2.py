class Solution:
    def subsetsWithDup(self, nums):
        res = set()

        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                print(res)
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)
        


        nums.sort()
        backtrack(0, [])
        print("ordered:")
        print(res)
        return [list(s) for s in res]
    

mylist = [4, 1, 3, 2]

solution = Solution()
solution.subsetsWithDup(mylist)