class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lt = 0
        seen = {}
        max_len = 0
        for rt, c in enumerate(s):
            if c in seen and seen[c] >= lt:
                lt = seen[c] + 1
            seen[c] = rt
            max_len = max(max_len, rt - lt + 1)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        ans = 0
        for char in s:
            while char in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(char)
            ans = max(ans, len(char_set))

        return ans
            