class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "A man, a plan, a canal: Panama",  # True
        "racecar",  # True
        "No lemon, no melon",  # True
        "hello",  # False
        "Was it a car or a cat I saw?",  # True
        "12321",  # True
        "12345",  # False
        "",  # True (empty string)
        "Able was I, ere I saw Elba!",  # True
    ]
    for s in test_cases:
        print(f"'{s}' -> {solution.isPalindrome(s)}")
