
class Solution(object):
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        n = len(nums)
        left = 0

        for i in range(n):
            right = total_sum - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1
