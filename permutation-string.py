class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr = sorted(subStr)
                if subStr == s1:
                    return True
        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        from collections import Counter
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            if Counter(s2[l:r + 1]) == Counter(s1):
                return True
            l += 1
        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution2().checkInclusion(s1, s2))  # Output: True

    s1 = "ab"
    s2 = "eidboaoo"
    print(Solution2().checkInclusion(s1, s2))  # Output: False