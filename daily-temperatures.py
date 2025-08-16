from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        n = len(temperatures)
        ans = [0] * n
        for i in range(1, n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)

        return ans


if __name__ == "__main__":
    solution = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures(temperatures))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    temperatures = [30, 40, 50, 60]
    print(solution.dailyTemperatures(temperatures))  # Output: [1, 1, 1, 0]
    temperatures = [30, 60, 90]
    print(solution.dailyTemperatures(temperatures))  # Output: [1, 1, 0]