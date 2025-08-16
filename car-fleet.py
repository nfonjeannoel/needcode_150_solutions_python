from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [(p, s) for p, s in zip(position, speed)]
        posAndSpeed.sort(reverse=True)
        stack = []
        for pos, carSpeed in posAndSpeed:
            time = (target - pos) / carSpeed
            if not stack:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
        return len(stack)







if __name__ == "__main__":
    sol = Solution()
    print(sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # Output: 3
    print(sol.carFleet(10, [3], [3]))  # Output: 1
    print(sol.carFleet(100, [0, 2, 4], [4, 2, 1]))  # Output: 1
