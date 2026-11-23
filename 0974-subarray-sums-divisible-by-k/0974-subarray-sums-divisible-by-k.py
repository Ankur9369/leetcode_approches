class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        t_sum=0
        sum_map={0:1}
        res=0
        
        for i in range(len(nums)):
            t_sum+=nums[i]
            remain=t_sum%k
            if remain in sum_map:
                res+=sum_map[remain]
            sum_map[remain]=sum_map.get(remain,0)+1
        return res
            
            