class MinStack(object):
    # use 2 stacks, one for normal values, one for minimums

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # if val is smaller or equal to current min, record it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        # always remove from main/value stack
        val = self.stack.pop()
        # if that value was the min, remove from min stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # this takes O(n) -> too long
        # min_so_far = self.stack[0]
        # for elem in self.stack:
        #     min_so_far = min(min_so_far, elem)
        # return min_so_far

        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()