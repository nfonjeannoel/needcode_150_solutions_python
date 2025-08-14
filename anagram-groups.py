from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for word in strs:
            word = "".join(sorted(word))
            print("Sorted word:", word)
            groups[word].append(word)

        print(groups)
        return list(groups.values())


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for char in strs:
            count = [0] * 26
            for i in char:
                count[ord(i) - ord('a')] += 1

            groups[tuple(count)].append(char)

        return list(groups.values())


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(input_strs)
    print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


