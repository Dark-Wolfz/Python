class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        a = len(words)
        left, right = 0, a-1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left +=1
            right -=1
        return ' '.join(words)
