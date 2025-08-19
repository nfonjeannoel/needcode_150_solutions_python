class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(t) > len(s) or not t or not s:
            return ""
        from collections import Counter
        need = Counter(t)
        have = {}
        required = len(need)
        formed = 0

        best_len = float('inf')
        best_l, best_r = 0, 0
        l = 0

        for r, ch in enumerate(s):
            if ch in need:
                have[ch] = 1 + have.get(ch, 0)
                if have[ch] == need[ch]:
                    formed += 1

            while formed == required:
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_l = l
                    best_r = r

                left_ch = s[l]
                if left_ch in need:
                    have[left_ch] -= 1
                    if have[left_ch] < need[left_ch]:
                        formed -= 1
                l += 1

        return "" if best_len == float('inf') else s[best_l: best_r + 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
    print(sol.minWindow("a", "a"))                # Output: "a"
    print(sol.minWindow("a", "aa"))               # Output: ""
    print(sol.minWindow("a", ""))                 # Output: ""
    print(sol.minWindow("", "a"))                 # Output: ""
    print(sol.minWindow("", ""))                  # Output: ""






