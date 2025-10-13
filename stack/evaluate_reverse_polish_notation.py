class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()  # right operand
                a = stack.pop()  # left operand

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack.pop()
        