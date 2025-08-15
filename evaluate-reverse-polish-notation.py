from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def is_operator(t):
            return t in ["+", "*", "-", "/"]

        def perform_operation(n1, n2, operation):
            n1, n2 = int(n1), int(n2)
            if operation == "*":
                return n1 * n2
            elif operation == "-":
                return n1 - n2
            elif operation == "+":
                return n1 + n2
            elif operation == "/":
                return int(n1 / n2)
            else:
                pass  # not defined

        for token in tokens:
            if is_operator(token):
                num2, num1 = stack.pop(), stack.pop()
                stack.append(perform_operation(num1, num2, token))
            else:
                stack.append(token)

        return int(stack.pop())


if __name__ == "__main__":
    solution = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    print(solution.evalRPN(tokens))  # Output: 9
    tokens = ["4", "13", "5", "/", "+"]
    print(solution.evalRPN(tokens))  # Output: 6