class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        best = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r - l + 1)
        return best


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            res = max(res, len(seen))

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
    print(sol.lengthOfLongestSubstring(""))           # Output: 0
    print(sol.lengthOfLongestSubstring("a"))          # Output: 1
    print(sol.lengthOfLongestSubstring("dvdf"))       # Output: 3