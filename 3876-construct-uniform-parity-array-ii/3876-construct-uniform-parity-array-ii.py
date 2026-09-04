class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Find smallestOdd
        odd = [x for x in nums1 if x % 2 != 0]
        # check it exist or not
        if not odd:
            return True

        smallest_odd = min(odd)
        # use loop and verify all element  whether it  smaller than  smallesr_odd or not:
        for num in  nums1:
            if num%2==0:
                if num < smallest_odd:
                    return False
        return  True
        
        