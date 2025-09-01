class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):  # n - 2 + 1 cause of 0 based index
            temp = one
            one = one + two
            two = temp
        return one


class Solution2:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)
