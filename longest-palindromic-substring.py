class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        res_start, res_len = 0, 0

        def expand(l: int, r: int):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # after loop, palindrome is s[l+1:r]
            return l + 1, r - l - 1

        for i in range(n):
            # odd
            start, length = expand(i, i)
            if length > res_len:
                res_start, res_len = start, length
            # even
            start, length = expand(i, i + 1)
            if length > res_len:
                res_start, res_len = start, length

        return s[res_start:res_start + res_len]
