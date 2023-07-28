class Solution(object):
    def twoSum(self, nums, target):
        a = []
        b = len(nums)
        left, right = 0, b - 1  # Corrected initialization of 'right'

        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ == target:
                a.append(left)
                a.append(right)
                return a
            elif left != right - 1:
                right -= 1
            else:
                right = b-1
                left += 1
        return a
