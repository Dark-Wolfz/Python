class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        b,c = 0 , len(a) - 1
        while b < c:
            if a[b] != a[c]:
                return False
            b += 1
            c -= 1
        return True
