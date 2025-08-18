class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        maxf = 0

        for r in range(len(s)):
            char = s[r]
            count[char] = 1 + count.get(char, 0)
            maxf = max(maxf, count[char])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        for i in range(len(s)):
            count = {}
            maxf = 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j], 0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("AABABBA", 1))  # Output: 4
    print(sol.characterReplacement("ABAB", 2))     # Output: 4
    print(sol.characterReplacement("AABBA", 1))    # Output: 4
    print(sol.characterReplacement("A", 0))        # Output: 1
    print(sol.characterReplacement("", 0))         # Output: 0