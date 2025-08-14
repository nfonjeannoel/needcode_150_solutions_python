from collections import defaultdict
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    char_count = defaultdict(int)
    for ch_s, ch_t in zip(s, t):
        char_count[ch_s] += 1
        char_count[ch_t] -= 1

    return all(count==0 for count in char_count.values())





