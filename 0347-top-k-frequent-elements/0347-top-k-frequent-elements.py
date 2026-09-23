class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        have={}
        for num in nums:
            if num not in have:
                have[num]=1
            else:have[num]+=1
        sorted_freq = sorted(have.items(), key=lambda x: x[1], reverse=True)

        result=[]
        for i in range(k):
            result.append(sorted_freq[i][0])

        return result