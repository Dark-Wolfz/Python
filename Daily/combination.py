class Solution(object):
    def combine(self, n, k):
        def backtrack(start, current_combination):
            if len(current_combination) == k:
                result.append(current_combination)
                return
            for i in range(start, n + 1):
                backtrack(i + 1, current_combination + [i])

        result = []
        backtrack(1, [])
        return result
