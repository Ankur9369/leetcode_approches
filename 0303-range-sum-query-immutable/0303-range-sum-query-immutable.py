class NumArray(object):

    def __init__(self, nums):
        self.prefix_sum = [0]

        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
