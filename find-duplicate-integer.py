from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return None

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            ind = abs(num) - 1
            if nums[ind] < 0:
                return abs(num)
            nums[ind] *= -1

        return -1