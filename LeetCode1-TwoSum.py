class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for i in range(0,len(nums)):
            diff = target-nums[i]
            if not diff in d:
               d[nums[i]] = i
            else:
                return [ i, d[diff]] 
