class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0,len(nums)-1

        while l<=r:    
        
         mid = (l+r)//2
         
         if nums[mid] == target:
               return mid   

            # check if left half is sorted; if yes, go right
         elif nums[mid] >= nums[l]: # left is sorted
              if nums[l] <= target <= nums[mid]:
                  r = mid -1
              else:
                  l = mid+1  
            # check if right half is sorted; if yes, go left   
            
         elif nums[mid] <= nums[r]:  
            if nums[mid] <= target <= nums[r]:
                l = mid+1
            else:
                r = mid-1    
        return -1       
