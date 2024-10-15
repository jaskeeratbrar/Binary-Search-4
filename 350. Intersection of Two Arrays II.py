class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        trackMap = {}

        res = []

        for i in nums1:
            if i in trackMap:
                trackMap[i] += 1
            else:
                trackMap[i] = 1

        
        for i in nums2:
            if i in trackMap and trackMap[i] > 0:
                res.append(i)
                trackMap[i] -= 1
        
        return res
        
### T(C) : O(M+N)
### S(C) : O(M) .... nums1 size
