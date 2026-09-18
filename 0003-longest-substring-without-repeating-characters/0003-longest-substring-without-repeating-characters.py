class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new = ""
        length = 0

        for i in range(len(s)):
            if s[i] in new:
                index = new.index(s[i])
                new = new[index + 1:]

            new += s[i]

            if len(new) > length:
                length = len(new)

        return length