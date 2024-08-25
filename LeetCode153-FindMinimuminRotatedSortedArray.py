class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0,len(nums)-1
        tgt = float('inf')


        while l<=r:    
         if nums[l] < nums[r]:
            tgt = min(tgt, nums[l])
            break

         mid = (l+r)//2
         tgt = min(tgt, nums[mid])
         if nums[l] <= nums[mid]:
            l = mid+1 
         else:
            r = mid -1
        return tgt      
