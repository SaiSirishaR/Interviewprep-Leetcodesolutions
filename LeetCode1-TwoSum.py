class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(0,len(nums)):
            diff = target-nums[i]
            if not diff in d:
               d[nums[i]] = i
            else:
                return [ i, d[diff]] 


####if the array is sorted

 #      l, r= 0, 1
       
 #      while l<r and r < len(nums):
 #       if nums[l] + nums[r] == target:
 #           return [l,r]
 #       elif nums[l] + nums[r] > target:
 #           r-=1
 #       elif nums[l] + nums[r] < target:
 #           l+=1
 #      return []
