from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] != '#':
                j += 1

            l = int(s[i:j])
            j = j + 1
            decoded.append(s[j:j + l])
            i = j + l

        return decoded


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    original_strings = ["hello", "world"]
    encoded_string = solution.encode(original_strings)
    print("Encoded:", encoded_string)
    decoded_strings = solution.decode(encoded_string)
    print("Decoded:", decoded_strings)
    assert original_strings == decoded_strings, "Decoded strings do not match original strings."
