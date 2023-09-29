class Solution:
    def search(self, nums: List[int], target: int) -> int:

       l ,r = 0, len(nums)-1

       while l<=r:

            mid = (l+r)//2

            if nums[mid] == target:
             return mid

         ## left sorted
            if nums[mid] > nums[mid-1]:
              if nums[mid] < target or target < nums[mid-1]:
                 l = mid+1
              else:
                 r = mid-1

        ## right sorted
            else:
              if nums[mid] > target or target > nums[mid+1]:
                 r = mid-1
              else:
                 l = mid+1
       return -1


        
