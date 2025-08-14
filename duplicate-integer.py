# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
def contains_duplicate(nums):
    char_set = set()
    for num in nums:
        if num in char_set:
            return True
        char_set.add(num)

    return False


# Test cases
def test_contains_duplicate():
    def status(got, expected):
        return "\033[91mFAIL\033[0m" if got != expected else "\033[92mPASS\033[0m"
    print(f"Test 1: Input: [1,2,3,1] | Expected: True | Got: {contains_duplicate([1,2,3,1])} | Status: {status(contains_duplicate([1,2,3,1]), True)}")
    print(f"Test 2: Input: [1,2,3,4] | Expected: False | Got: {contains_duplicate([1,2,3,4])} | Status: {status(contains_duplicate([1,2,3,4]), False)}")
    print(f"Test 3: Input: [1,1,1,3,3,4,3,2,4,2] | Expected: True | Got: {contains_duplicate([1,1,1,3,3,4,3,2,4,2])} | Status: {status(contains_duplicate([1,1,1,3,3,4,3,2,4,2]), True)}")
    print(f"Test 4: Input: [] | Expected: False | Got: {contains_duplicate([])} | Status: {status(contains_duplicate([]), False)}")
    print(f"Test 5: Input: [0] | Expected: False | Got: {contains_duplicate([0])} | Status: {status(contains_duplicate([0]), False)}")

if __name__ == "__main__":
    test_contains_duplicate()
