class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # for odd
        canOdd=True
        for num in nums1:
            if num%2==0:# even 
                found=False

                for x in nums1: 
                    if x%2==1 and num > x:
                        found= True
                        break
                if not found:
                    canOdd=  False
                    break
        # for even            
        caneven=True
        for num in nums1:
            if num%2==1:# odd
                found=False

                for x in nums1 :
                    if x%2==0 and num > x:
                        found= True
                        break
                if not found:
                    caneven=  False
                    break
        return canOdd or caneven
                

            
           
           
                
        

        