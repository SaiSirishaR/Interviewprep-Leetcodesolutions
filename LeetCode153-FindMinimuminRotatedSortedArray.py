class Solution:
    def findMin(self, nums: List[int]) -> int:
        
# Case 1: if left most element is less than the right most element
# Case 2: if the mid elements is less than the previous and next element
# Case 3: if mid+1 [or r] is > mid then right side is sorted, go to left vice versa

        l ,r =0, len(nums)-1
       
        while l<=r:
            # Case 1

            if nums[l] < nums[r]: 
                return nums[l]
            mid = (l+r)//2

             # Case 2

            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
               return nums[mid]  

             # Case 3

            if nums[mid] < nums[r]: 
                r = mid -1
            else:
                l = mid+1           

        
