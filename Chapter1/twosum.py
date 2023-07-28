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

# Another solution
class Solution(object):
    def twoSum(self, nums, target):
        a = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums and nums.index(complement) != i:
                a.append(i)
                a.append(nums.index(complement))
                return a
        return a
# Using dictionary
class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []
