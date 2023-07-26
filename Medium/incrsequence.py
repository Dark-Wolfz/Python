class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        first = second = float ('inf')
        second = float ('inf')
        for num in nums:
            if num <= first:
                first = num
            elif first < num <= second:
                second = num
            elif num > second:
                return True
            else:
                return False

or optimized using list of length 3

//class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        if n<3:
            return False
        seq = [float('inf')] * 3
        for num in nums:
            if num <= seq[0]:
                seq[0] = num
            elif num <= seq[1]:
                seq[1] = num
            else:
                return True
        return False

