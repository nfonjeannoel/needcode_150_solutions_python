from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for ind1, num1 in enumerate(nums):
            prod = 1
            for ind2, num2 in enumerate(nums):
                if ind1 == ind2:
                    continue
                prod *= num2
            answer.append(prod)

        return answer


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n
        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res


class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_count = 0
        total_prod = 1
        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                total_prod *= num

        n = len(nums)
        res = [0] * n

        if zeros_count > 1:
            return res

        if zeros_count == 1:
            for ind, i in enumerate(nums):
                if i == 0:
                    res[ind] = total_prod
                else:
                    res[ind] = 0
            return res

        for ind, i in enumerate(nums):
            res[ind] = total_prod // i

        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    result = solution.productExceptSelf(nums)
    print("Product of array except self:", result)
    # Expected output: [24, 12, 8, 6]
    assert result == [24, 12, 8, 6], "The product array does not match the expected output."
