class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0

            if s[i] == "(":
                return dfs(i + 1, open + 1)
            elif s[i] == ")":
                return dfs(i + 1, open - 1)
            else:
                return (
                        dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open - 1)
                )

        return dfs(0, 0)


class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        n = len(s)

        def dfs(i, open):
            if open < 0:
                return False
            if open > n - i:
                return False
            if i == len(s):
                return open == 0

            if (i, open) in memo:
                return memo[(i, open)]

            if s[i] == "(":
                ans = dfs(i + 1, open + 1)
            elif s[i] == ")":
                ans = dfs(i + 1, open - 1)
            else:
                ans = (
                        dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open - 1)
                )
            memo[(i, open)] = ans
            return ans

        return dfs(0, 0)
