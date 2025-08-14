from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    left_val = nums[l]
                    right_val = nums[r]
                    while l < r and left_val == nums[l]:
                        l += 1
                    while l < r and right_val == nums[r]:
                        r -= 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
    print(sol.threeSum([]))                      # Output: []
    print(sol.threeSum([0]))                     # Output: []
    print(sol.threeSum([0, 0, 0]))               # Output: [[0, 0, 0]]
    print(sol.threeSum([-2, 0, 1, 1, 2]))        # Output: [[-2, 0, 2], [-2, 1, 1]]