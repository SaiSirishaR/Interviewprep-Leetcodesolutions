class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = []
        b = [[] for i in range(len(nums))]
        fmul = 1
        bmul = 1
        res = []

        j = len(nums)-1
        for ii in range(len(nums)):
            f.append(fmul)
            fmul = fmul*nums[ii]
            b[j] = bmul
            bmul = bmul*nums[j]
            j -=1
        
        for kk in range(len(f)):
           res.append(f[kk]*b[kk])
    
        return res
