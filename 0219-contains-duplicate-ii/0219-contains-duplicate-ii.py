class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        have={}
        for i in range(len(nums)):
            element=nums[i]
            if element in have:
                prev=have[element]
                if i-prev<= k:
                    return True
            have[element]=i
        return False
        