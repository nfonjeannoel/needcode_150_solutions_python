class Solution:
    def isValid(self, s: str) -> bool:
        cto = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []
        for b in s:
            if b in cto:
                if stack and stack[-1] == cto[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)


        if not stack:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "()",         # True
        "()[]{}",     # True
        "(]",         # False
        "([)]",       # False
        "{[]}",       # True
        "",           # True (empty string)
        "((()))",     # True (nested parentheses)
        "(()",        # False (unmatched opening parenthesis)
        "())",        # False (unmatched closing parenthesis)
        "[{()}]",     # True (mixed types)
    ]

    for case in test_cases:
        print(f"{case}: {solution.isValid(case)}")