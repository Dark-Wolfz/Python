class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest_len = 0
        substring = ""

        if len(s) == 0: 
            return 0

        for ch in s:
            if ch not in substring:
                substring += ch
            else:
                if longest_len < len(substring):
                    longest_len = len(substring)
                index = substring.index(ch)
                substring = substring[index + 1:] + ch

        if longest_len < len(substring):
            longest_len = len(substring)

        return longest_len
