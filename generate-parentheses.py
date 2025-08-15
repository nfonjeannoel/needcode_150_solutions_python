from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [(0, 0, "")]
        res = []
        while stack:
            openN, closeN, s = stack.pop()

            if openN == closeN == n:
                res.append(s)
                continue

            if openN < n:
                stack.append((openN + 1, closeN, s + "("))

            if closeN < openN:
                stack.append((openN, closeN + 1, s + ")"))

        return res


if __name__ == "__main__":
    solution = Solution()
    n = 3
    print(solution.generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
    n = 1
    print(solution.generateParenthesis(n))  # Output: ["()"]
