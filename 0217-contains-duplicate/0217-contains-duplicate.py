class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dup = {}

        for num in range(len(nums)):

            if nums[num] not in dup:
                dup[nums[num]] = 1
            else:
                dup[nums[num]] += 1

        for i in dup:
            if dup[i] >= 2:
                return True

        return False