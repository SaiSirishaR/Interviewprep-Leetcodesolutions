class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 

        d = set()
        for i in range(0,len(nums)): # for i, vallue in enumerate(nums):
            if nums[i] not in d:
                d.add(nums[i])
            else:
                return True
        return False
