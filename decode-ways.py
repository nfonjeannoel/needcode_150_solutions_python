class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # base case: 1 way to decode an empty string at the end

        def dfs(i):
            if i in dp:
                return dp[i]  # memoization (reuse pre-computed answers)

            if s[i] == '0':  # cannot decode strings starting with '0'
                return 0

            # Choice 1: decode single digit
            res = dfs(i + 1)

            # Choice 2: decode two digits (if valid 10–26)
            if (i + 1) < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                res += dfs(i + 2)

            dp[i] = res  # store result in dp
            return res

        return dfs(0)

class Solution2:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}   # base case: 1 way to decode an empty string at the end

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
        return dp[0]

